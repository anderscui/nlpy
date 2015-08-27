# coding=utf-8
from __future__ import absolute_import, unicode_literals

__version__ = '0.37'
__license__ = 'MIT'

import re
import os
import sys
import time
import logging
import threading
import marshal
import tempfile

from math import log
from hashlib import md5

from _compat import *
import finalseg

# set _replace_file function.
if os.name == 'nt':
    from shutil import move as _replace_file
else:
    _replace_file = os.rename

_get_module_path = lambda path: os.path.normpath(os.path.join(os.getcwd(),
                                                              os.path.dirname(__file__), path))
_get_abs_path = lambda path: os.path.normpath(os.path.join(os.getcwd(), path))

# default dict file under current dir.
DEFAULT_DICT = _get_module_path("dict.txt")

log_console = logging.StreamHandler(sys.stderr)
default_logger = logging.getLogger(__name__)
default_logger.setLevel(logging.DEBUG)
default_logger.addHandler(log_console)

DICT_WRITING = {}

pool = None

# re.U: Make \w, \W, \b, \B, \d, \D, \s and \S dependent on the Unicode character properties database.
re_eng = re.compile('[a-zA-Z0-9]', re.U)

# \u4E00-\u9FA5a-zA-Z0-9+#&\._ : All non-space characters. Will be handled with re_han
# \r\n|\s : whitespace characters. Will not be handled.
re_han_default = re.compile("([\u4E00-\u9FA5a-zA-Z0-9+#&\._]+)", re.U)
re_skip_default = re.compile("(\r\n|\s)", re.U)
re_han_cut_all = re.compile("([\u4E00-\u9FA5]+)", re.U)
re_skip_cut_all = re.compile("[^a-zA-Z0-9+#\n]", re.U)


# def setLogLevel(log_level):
#     global logger
#     default_logger.setLevel(log_level)


class Tokenizer(object):
    def __init__(self, dictionary=DEFAULT_DICT):
        self.lock = threading.RLock()
        self.dictionary = _get_abs_path(dictionary)
        self.FREQ = {}
        self.total = 0
        self.user_word_tag_tab = {}
        self.initialized = False
        self.tmp_dir = None
        self.cache_file = None

    def __repr__(self):
        return '<Tokenizer dictionary=%r>' % self.dictionary

    def gen_pfdict(self, f_name):
        lfreq = {}
        ltotal = 0
        with open(f_name, 'rb') as f:
            for lineno, line in enumerate(f, 1):
                try:
                    line = line.strip().decode('utf-8')
                    word, freq = line.split(' ')[:2]
                    freq = int(freq)
                    lfreq[word] = freq
                    ltotal += freq
                    for ch in xrange(len(word)):
                        wfrag = word[:ch + 1]
                        if wfrag not in lfreq:
                            lfreq[wfrag] = 0
                except ValueError:
                    raise ValueError(
                        'invalid dictionary entry in %s at Line %s: %s' % (f_name, lineno, line))
        return lfreq, ltotal

    def initialize(self, dictionary=None):
        if dictionary:

            abs_path = _get_abs_path(dictionary)
            if self.dictionary == abs_path and self.initialized:
                return
            else:
                self.dictionary = abs_path
                self.initialized = False
        else:
            abs_path = self.dictionary

        print abs_path

        with self.lock:
            try:
                with DICT_WRITING[abs_path]:
                    pass
            except KeyError:
                pass
            if self.initialized:
                return

            default_logger.debug("Building prefix dict from %s ..." % abs_path)
            t1 = time.time()

            # get cache file path
            if self.cache_file:
                cache_file = self.cache_file
            # default dictionary
            elif abs_path == DEFAULT_DICT:
                cache_file = "jieba.cache"
            # custom dictionary
            else:
                cache_file = "jieba.u%s.cache" % md5(abs_path.encode('utf-8', 'replace')).hexdigest()

            cache_file = os.path.join(self.tmp_dir or tempfile.gettempdir(), cache_file)
            # prevent absolute path in self.cache_file
            tmpdir = os.path.dirname(cache_file)

            #
            load_from_cache_fail = True
            if os.path.isfile(cache_file) and os.path.getmtime(cache_file) > os.path.getmtime(abs_path):
                default_logger.debug("Loading model from cache %s" % cache_file)
                try:
                    with open(cache_file, 'rb') as cf:
                        self.FREQ, self.total = marshal.load(cf)
                    load_from_cache_fail = False
                except Exception:
                    load_from_cache_fail = True

            if load_from_cache_fail:
                wlock = DICT_WRITING.get(abs_path, threading.RLock())
                DICT_WRITING[abs_path] = wlock
                with wlock:
                    self.FREQ, self.total = self.gen_pfdict(abs_path)
                    default_logger.debug("Dumping model to file cache %s" % cache_file)
                    try:
                        # prevent moving across different filesystems
                        fd, fpath = tempfile.mkstemp(dir=tmpdir)
                        with os.fdopen(fd, 'wb') as temp_cache_file:
                            marshal.dump((self.FREQ, self.total), temp_cache_file)
                        _replace_file(fpath, cache_file)
                    except Exception:
                        default_logger.exception("Dump cache file failed.")
                try:
                    del DICT_WRITING[abs_path]
                except KeyError:
                    pass

            self.initialized = True
            default_logger.debug(
                "Loading model cost %.3f seconds." % (time.time() - t1))
            default_logger.debug("Prefix dict has been built succesfully.")

    def check_initialized(self):
        if not self.initialized:
            self.initialize()

    def get_DAG(self, sentence):
        self.check_initialized()
        DAG = {}
        N = len(sentence)
        for k in xrange(N):
            tmplist = []
            i = k
            frag = sentence[k]
            while i < N and frag in self.FREQ:
                if self.FREQ[frag]:
                    tmplist.append(i)
                i += 1
                frag = sentence[k:i + 1]
            if not tmplist:
                tmplist.append(k)
            DAG[k] = tmplist
        return DAG

    def calc(self, sentence, DAG, route):
        N = len(sentence)
        route[N] = (0, 0)
        logtotal = log(self.total)
        for idx in xrange(N - 1, -1, -1):

            print [(log(self.FREQ.get(sentence[idx:x + 1]) or 1) -
                    logtotal + route[x + 1][0], x) for x in DAG[idx]]

            route[idx] = max((log(self.FREQ.get(sentence[idx:x + 1]) or 1) -
                              logtotal + route[x + 1][0], x) for x in DAG[idx])


if __name__ == '__main__':
    tokenizer = Tokenizer()

    # gen trie
    # freqs, total = tokenizer.gen_pfdict(DEFAULT_DICT)


    # tokenizer.initialize()
    # freqs, total = tokenizer.FREQ, tokenizer.total
    # for k in freqs:
    #     print k, freqs[k]

    tokenizer.initialize()
    print len(tokenizer.FREQ)
    print tokenizer.total

    sentence = u'我很喜欢刺客聂隐娘这部电影'
    #sentence = u'语言学家 参加 学术会议'
    # sentence = u'说曹操曹操到'
    # DAG:
    dag = tokenizer.get_DAG(sentence)
    # print(dag)

    route = {}
    # tokenizer.calc(sentence, dag, route)
    # print(route)

    sentence = u'我先是学习了C，后面又学了Python 2.7, Java 8等等'
    finalseg.cut(sentence)
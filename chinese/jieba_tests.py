# coding: utf-8
import os
import jieba
import jieba.posseg as pseg
from common.chinese import read_lines, write


lines = read_lines('jieba_test.txt')


def gen_test_result(fname, cut_all=False, HMM=True):
    result = ["/ ".join(jieba.cut(s.strip(), cut_all, HMM)) for s in lines]
    write(fname, os.linesep.join(result))


def gen_test_search_result(fname, HMM=True):
    result = ["/ ".join(jieba.cut_for_search(s.strip(), HMM)) for s in lines]
    write(fname, os.linesep.join(result))


def get_str_of_pos_tag(pos_tag):
    return '%s/%s' % (pos_tag.word, pos_tag.flag)


def gen_test_pos_cut_result(fname, HMM=True):
    result = []
    for s in lines:
        line_cut = [get_str_of_pos_tag(tag) for tag in pseg.cut(s.strip(), HMM)]
        result.append(" ".join(line_cut))
    write(fname, os.linesep.join(result))


gen_test_result('accurate_hmm.txt')
gen_test_result('accurate_no_hmm.txt', HMM=False)
gen_test_result('cut_all.txt', cut_all=True)

gen_test_search_result('cut_search_hmm.txt', HMM=True)
gen_test_search_result('cut_search_no_hmm.txt', HMM=False)

gen_test_pos_cut_result('pos_cut_hmm.txt', HMM=True)
gen_test_pos_cut_result('pos_cut_no_hmm.txt', HMM=False)



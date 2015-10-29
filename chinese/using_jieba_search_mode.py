# coding: utf-8
import jieba
from jieba.analyse.analyzer import ChineseTokenizer


def cuttest(text):
    tokens = jieba.tokenize(text, mode="search")
    print "搜索：", "/ ".join([t[0] for t in tokens])

cuttest(u'机器学习')
cuttest(u'自然语言处理')

jieba.add_word(u'机器学习')
jieba.add_word(u'自然语言处理')

cuttest(u'机器学习')
cuttest(u'自然语言')
cuttest(u'自然语言处理')


tokens = jieba.tokenize(u'语言学家参加学术会议', mode="search")
tokens = [t[0] for t in tokens]
for t in tokens:
    print t
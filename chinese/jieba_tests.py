# coding: utf-8
import os
import jieba
from common.chinese import read_lines, write


lines = read_lines('jieba_test.txt')


def gen_test_result(fname, cut_all=False, HMM=True):
    result = ["/ ".join(jieba.cut(s.strip(), cut_all, HMM)) for s in lines]
    write(fname, os.linesep.join(result))


def gen_test_search_result(fname, HMM=True):
    result = ["/ ".join(jieba.cut_for_search(s.strip(), HMM)) for s in lines]
    write(fname, os.linesep.join(result))


gen_test_result('accurate_hmm.txt')
gen_test_result('accurate_no_hmm.txt', HMM=False)
gen_test_result('cut_all.txt', cut_all=True)

gen_test_search_result('cut_search_hmm.txt', HMM=True)
gen_test_search_result('cut_search_no_hmm.txt', HMM=False)




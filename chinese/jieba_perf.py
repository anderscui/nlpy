# from __future__ import unicode_literals
# coding: utf-8
import os
import jieba
import time
from common.chinese import read_all

text = read_all(u'围城.txt')
print os.path.getsize(u'围城.txt')

jieba.cut('热身一下')


# print len(text)
# seg_list = jieba.cut(text, cut_all=False, HMM=True)
# print "全模式：", "/ ".join(seg_list)

n = 10

t1 = time.time()
for i in range(n):
    l = list(jieba.cut(text))
seconds = time.time() - t1
print(seconds)

t1 = time.time()
for i in range(n):
    l = list(jieba.cut(text, cut_all=True))
seconds = time.time() - t1
print(seconds)
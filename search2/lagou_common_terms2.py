# coding=utf-8
from common.persistence import from_pickle

cnt_words = from_pickle('cnt_words.pkl')
cnt_word_doc = from_pickle('cnt_word_doc.pkl')

# for k in cnt_words.most_common(500):
#     print u'{0}: {1}'.format(k[0], k[1])
#
# print
# print
# print '++in docs++'
for k in cnt_word_doc.most_common(500):
    print u'{0}: {1}'.format(k[0], k[1])
    # print k[0]

# print(len(cnt_words))
#
# total_occr = 0
# top100
#
#
# def show_cnt(k):
#     print k, cnt_word_doc[k]
#
# show_cnt('R')
# show_cnt('r')
# show_cnt('C')
# show_cnt('C++')
# show_cnt('Java')
# show_cnt('Shell')
# show_cnt('Python')
# show_cnt('Ruby')
# show_cnt('Hadoop')
# show_cnt('Spark')

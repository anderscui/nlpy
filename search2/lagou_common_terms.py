# coding=utf-8
from collections import Counter
import datetime
import jieba
from common.html_util import strip_tags
from common.persistence import from_pickle, to_pickle

import sqlite3 as sqlite

con = sqlite.connect('lagou.db')

with con:
    con.row_factory = sqlite.Row
    cur = con.cursor()
    cur.execute("select * from position")
    # cur.execute("select * from position where name like '%Python%' "
    #             "or name like '%机器学习%' or name like '%数据挖掘%' or name like '%自然语言处理%' "
    #             "or name like '%C#%' or name like '%搜索算法%' or name like '%Hadoop%' "
    #             "or name like '%交互设计师%' or name like '%数据分析师%' or name like '%Java%'")
rows = cur.fetchall()

print(len(rows))

n = 1000000
cnt_word_doc = Counter()
cnt_words = Counter()
for pos in rows[:n]:
    desc = strip_tags(pos['desc'])
    tokens = jieba.tokenize(desc, mode="search")
    words = [t[0] for t in tokens]
    cur = Counter(words)
    for k in cur:
        cnt_word_doc[k] += 1
        cnt_words[k] += cur[k]

to_pickle(cnt_words, 'cnt_words.pkl')
to_pickle(cnt_word_doc, 'cnt_word_doc.pkl')
# rows = from_pickle('pos_list.pkl')

for k in cnt_words.most_common(200):
    print u'{0}: {1}'.format(k[0], k[1])

print
print
print '++in docs++'
for k in cnt_word_doc.most_common(200):
    print u'{0}: {1}'.format(k[0], k[1])

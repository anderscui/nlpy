# coding=utf-8
from common.html_util import strip_tags
from common.persistence import from_pickle

import sqlite3 as sqlite

con = sqlite.connect('lagou.db')

with con:

    con.row_factory = sqlite.Row
    cur = con.cursor()
    cur.execute("select * from position where name like '%Python%' "
                "or name like '%机器学习%' or name like '%数据挖掘%' or name like '%自然语言处理%' "
                "or name like '%C#%' or name like '%搜索算法%' or name like '%Hadoop%' "
                "or name like '%交互设计师%' or name like '%数据分析师%' or name like '%Java%'")
    rows = cur.fetchall()

    # print(type(rows))
    print(len(rows))

    # pos_list = [{'id': row['id'], 'pos_id': row['pos_id'], 'name': row['name'],
    #              'city': row['city']} for row in rows]
    # print(pos_list[0])


import sys, os
#
# sys.path.append("../")
from whoosh.index import create_in
from whoosh.fields import *

from jieba.analyse import ChineseAnalyzer

analyzer = ChineseAnalyzer()

schema = Schema(id=ID(stored=True),
                name=TEXT(stored=True),
                desc=TEXT(stored=True, analyzer=analyzer),
                city=TEXT(stored=True),
                salary=TEXT(stored=True),
                time_type=TEXT(stored=True),
                fin_stage=TEXT(stored=True),
                industry=TEXT(stored=True),
                advantage=TEXT(stored=True, analyzer=analyzer),
                com_name=TEXT(stored=True, analyzer=analyzer),
                address=TEXT(stored=True))

idx_dir = 'lagou_idx'
if not os.path.exists(idx_dir):
    os.mkdir(idx_dir)

ix = create_in(idx_dir, schema)  # for create new index
# ix = open_dir(idx_dir)  # for read only
writer = ix.writer()

# n = 10
n = len(rows)
for pos in rows[:n]:

    # print(pos['name'])
    # print(pos['pos_id'])
    # print(pos['city'])
    # print(strip_tags(pos['desc']))

    writer.add_document(
        id=unicode(pos['pos_id']),
        name=unicode(pos['name']),
        desc=unicode(strip_tags(pos['desc'])),
        city=pos['city']
    )

    # print('')

writer.commit()
# coding=utf-8
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

# print(type(rows))
print(len(rows))

# pos_list = [{'id': row['id'], 'pos_id': row['pos_id'], 'name': row['name'],
# 'city': row['city']} for row in rows]
# print(pos_list[0])

# to_pickle(rows, 'pos_list.pkl')

# rows = from_pickle('pos_list.pkl')
# print(len(rows))
# print(type(rows))
# print(rows[0])


import os
from whoosh.index import create_in
from whoosh.fields import *

from jieba.analyse import ChineseAnalyzer

stopwords = list(from_pickle('stopwords.pkl'))
analyzer = ChineseAnalyzer(stopwords)

schema = Schema(id=ID(stored=True),
                name=TEXT(stored=True, analyzer=analyzer),
                desc=TEXT(analyzer=analyzer),
                city=TEXT(stored=True),
                salary=TEXT(stored=True),
                salary_from=NUMERIC(int, 32, signed=False, stored=True),
                salary_to=NUMERIC(int, 32, signed=False, stored=True),
                # time_type=TEXT(stored=True),
                fin_stage=TEXT(stored=True),
                industry=TEXT(stored=True),
                education=TEXT(stored=True),
                advantage=TEXT(stored=True, analyzer=analyzer),
                com_name=TEXT(stored=True, analyzer=analyzer),
                address=TEXT(stored=True),
                date=DATETIME(stored=True, sortable=True))

idx_dir = 'lagou_idx'
if not os.path.exists(idx_dir):
    os.mkdir(idx_dir)

ix = create_in(idx_dir, schema)  # for create new index
# ix = open_dir(idx_dir)  # for read only
writer = ix.writer()


def parse_time(s):
    if '.' in s:
        return datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S.%f')
    else:
        return datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')


def parse_salary(s):
    m = re.search(u'(\d+)k以上', s)
    if m:
        return int(m.group(1)) * 1000, 10 ** 6

    m = re.search(u'(\d+)k以下', s)
    if m:
        return 0, int(m.group(1)) * 1000

    m = re.search(u'(\d+)k-(\d+)k', s)
    if m:
        return int(m.group(1)) * 1000, int(m.group(2)) * 1000
    return 0, 0


# n = 10
n = len(rows)
for pos in rows[:n]:
    # print(pos['name'])
    # print(pos['pos_id'])
    # print(pos['city'])
    # print(strip_tags(pos['desc']))
    salary_range = parse_salary(pos['salary'])

    writer.add_document(
        id=unicode(pos['pos_id']),
        name=pos['name'],
        desc=unicode(strip_tags(pos['desc'])),
        city=pos['city'],
        salary=pos['salary'],
        salary_from=salary_range[0],
        salary_to=salary_range[1],
        # time_type=pos['time_type'],
        fin_stage=pos['fin_stage'],
        industry=pos['industry'],
        education=pos['education'],
        advantage=pos['advantage'],
        com_name=pos['com_name'],
        address=pos['com_address'],
        date=parse_time(pos['create_time'])
    )

    # print('')

writer.commit()
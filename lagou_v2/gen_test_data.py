# coding=utf-8
import sqlite3 as sqlite
from common.html_util import strip_tags
from common.persistence import to_pickle, from_pickle

con = sqlite.connect('lagou.db')

with con:

    con.row_factory = sqlite.Row
    cur = con.cursor()
    cur.execute("select * from position where subcategory in ('后端开发', '前端开发', '用户研究')")
    rows = cur.fetchall()

    positions = []
    for row in rows:
        if row['desc'] != 'n/a':
            positions.append((row['pos_id'], row['name'], row['industry'], row['desc']))

    print(len(positions))
    for p in positions[0]:
        print p

    to_pickle(positions, 'positions.pkl')

#####
raw_positions = positions
pos_dict = {}
for rp in raw_positions:
    pos_dict[int(rp[0])] = (rp[1], rp[2], strip_tags(rp[3]))

to_pickle(pos_dict, 'pos_norm.pkl')

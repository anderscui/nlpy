# coding=utf-8
from common.html_util import strip_tags
from common.persistence import from_pickle

jobs = from_pickle('../crawlers/unified.pkl')
for k in jobs.keys()[:2]:
    v = jobs[k]
    print(v['title'])
    print(v['city'])
    print(v['desc'])
    print('+++++')

import sys, os

sys.path.append("../")
from whoosh.index import create_in
from whoosh.fields import *

from jieba.analyse import ChineseAnalyzer

analyzer = ChineseAnalyzer()

schema = Schema(title=TEXT(stored=True),
                path=ID(stored=True),
                desc=TEXT(stored=True, analyzer=analyzer),
                city=TEXT(stored=True))

idx_dir = 'lagou'
if not os.path.exists(idx_dir):
    os.mkdir(idx_dir)

ix = create_in(idx_dir, schema)  # for create new index
# ix = open_dir(idx_dir)  # for read only
writer = ix.writer()

for j in jobs.values()[::10]:

    desc = j['desc'] if j['desc'] else u'无'
    city = j['city'] if j['city'] else u'未知'

    print(j['title'])
    print(j['job_id'])
    print(city)
    print(strip_tags(desc))

    writer.add_document(
        title=unicode(j['title']),
        path=unicode('/' + str(j['job_id'])),
        desc=unicode(strip_tags(desc)),
        city=city
    )

    print('')

writer.commit()
# coding=utf-8
import os

from whoosh.index import open_dir
from jieba.analyse import ChineseAnalyzer
from whoosh.qparser import QueryParser

analyzer = ChineseAnalyzer()

idx_dir = 'lagou_idx'
ix = open_dir(idx_dir)
searcher = ix.searcher()

parser = QueryParser("desc", schema=ix.schema)


k = u'自然语言处理 (city:上海 OR city:北京)'
q = parser.parse(k)
results = searcher.search(q)
print(u'{0} results found for keyword {1}: '.format(len(results), k))
for hit in results[:20]:
    print(hit['name'])
    print(hit['city'])
    print(hit['id'])
    # print(hit['desc'])
    print('************')
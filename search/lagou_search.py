# coding=utf-8
import os

from whoosh.index import create_in, open_dir
from whoosh.fields import *
from jieba.analyse import ChineseAnalyzer
from whoosh.qparser import QueryParser

analyzer = ChineseAnalyzer()

schema = Schema(title=TEXT(stored=True),
                path=ID(stored=True),
                content=TEXT(stored=True, analyzer=analyzer),
                city=TEXT(stored=True))

idx_dir = 'lagou'
ix = open_dir(idx_dir)
searcher = ix.searcher()

parser = QueryParser("desc", schema=ix.schema)


# while True:
#     qs = raw_input(u'Input your 关键字: '.encode(sys.stdout.encoding))
#     qs = qs.decode(sys.stdout.encoding)
#     q = parser.parse(qs)
#     results = searcher.search(q)
#     print(u'{0} results found for keyword {1}: '.format(len(results), qs))
#     for hit in results:
#         print(hit['title'])
#         print(hit['city'])
#         print(hit['path'])
#         print(hit['desc'])
#         print('************')
#     break


k = u'自然语言 (city:上海 OR city:北京)'
q = parser.parse(k)
results = searcher.search(q)
print(u'{0} results found for keyword {1}: '.format(len(results), k))
for hit in results:
    print(hit['title'])
    print(hit['city'])
    print(hit['path'])
    print(hit['desc'])
    print('************')
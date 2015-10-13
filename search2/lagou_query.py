# coding=utf-8
from whoosh import scoring
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh import query

idx_dir = 'lagou_idx'
ix = open_dir(idx_dir)
searcher = ix.searcher()

from whoosh import qparser
og = qparser.OrGroup.factory(0.9)
parser = QueryParser("desc", schema=ix.schema, group=og)

# Single field parser.
k = u'Java Python city:上海'
q = parser.parse(k)

results = searcher.search_page(q, 1, pagelen=5)

print(u'{0} results found for keyword {1}, {2} returned: '.format(len(results), k, results.scored_length()))
for hit in results[:50]:
    print(hit['id'])
    print(hit['name'])
    # print(hit['city'])
    print(hit['com_name'])
    print('************')

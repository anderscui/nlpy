# coding=utf-8
from whoosh.index import open_dir
from whoosh.qparser import MultifieldParser

idx_dir = 'lagou_idx'
ix = open_dir(idx_dir)
searcher = ix.searcher()

parser = MultifieldParser(["name", "desc"], schema=ix.schema)

# Single field parser.
k = u'数据挖掘 city:上海'
q = parser.parse(k)

results = searcher.search(q, limit=100)

print(u'{0} results found for keyword {1}, {2} returned: '.format(len(results), k, results.scored_length()))
for hit in results[:50]:
    print(hit['id'])
    print(hit['name'])
    # print(hit['city'])
    print(hit['com_name'])
    print('************')


keywords = [kw for kw, score in results.key_terms("desc", docs=100, numterms=10)]
for kw in keywords:
    print kw,
# coding=utf-8
import datetime
from whoosh.index import open_dir
from whoosh.qparser import MultifieldParser

idx_dir = 'lagou_idx'
ix = open_dir(idx_dir)
searcher = ix.searcher()

parser = MultifieldParser(["name", "com_name"], schema=ix.schema)

# Single field parser.
k = u'自然 语言 自然语言 处理 salary_from:[1 TO 5000] salary_to:[ TO 5000] city:上海'
q = parser.parse(k)

today = datetime.datetime.now()
date_to = today
date_from = today + datetime.timedelta(days=-7)
print date_to.strftime('%Y%m%d')
print date_from.strftime('%Y%m%d')

results = searcher.search_page(q, 1, pagelen=30)

print(u'{0} results found for keyword {1}, {2} returned: '.format(len(results), k, results.scored_length()))
for hit in results[:50]:
    print(hit['id'])
    print(hit['name'])
    print(hit['salary_from'], hit['salary_to'])
    print(hit['date'])
    print('************')


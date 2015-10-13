# coding=utf-8
from whoosh import scoring
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh import query

idx_dir = 'lagou_idx'
ix = open_dir(idx_dir)
searcher = ix.searcher()

parser = QueryParser("name", schema=ix.schema)

# k = u'Python (city:上海 OR city:杭州)'
k = u'自然语言处理 city:上海 (education:本科 OR education:硕士)'
q = parser.parse(k)

# default search
# results = searcher.search(q, limit=10)

# paging
# results = searcher.search_page(q, 1)

# print(u'{0} results found for keyword {1}, {2} returned: '.format(len(results), k, results.scored_length()))
# for hit in results[:50]:
#     print(hit['id'])
#     print(hit['name'])
#     # print(hit['city'])
#     print(hit['com_name'])
#     print('************')

# scoring
# with ix.searcher(weighting=scoring.TF_IDF()) as s:
#     results = s.search_page(q, 1)
#
#     print(u'{0} results found for keyword {1}, {2} returned: '.format(len(results), k, results.scored_length()))
#     for hit in results[:50]:
#         print(hit['id'])
#         print(hit['name'])
#         # print(hit['city'])
#         print(hit['com_name'])
#         print('************')


# filtering
k = u'自然语言处理'
q = parser.parse(k)

allow_q = query.Term("city", u"上海")
restrict_q = query.Term('education', u'硕士')

results = searcher.search(q, filter=allow_q, mask=restrict_q)

print(u'{0} results found for keyword {1}, {2} filtered out, {3} returned: '.format(len(results), k,
                                                                                    results.filtered_count,
                                                                                    results.scored_length()))
for hit in results[:50]:
    print(hit['id'])
    print(hit['name'])
    # print(hit['city'])
    print(hit['com_name'])
    print('************')

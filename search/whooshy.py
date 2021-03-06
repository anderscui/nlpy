from whoosh.index import create_in
from whoosh.fields import *

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
ix = create_in('idx', schema)
writer = ix.writer()
writer.add_document(title=u'First Document', path=u'/a',
                    content=u'This is the first document we have added!')
writer.add_document(title=u'Second Document', path=u'/b',
                    content=u'The second one is even more interesting!')
writer.commit()

from whoosh.qparser import QueryParser
with ix.searcher() as searcher:
    query = QueryParser('content', ix.schema).parse('first')
    results = searcher.search(query)
    for hit in results:
        print(hit)
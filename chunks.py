from nltk import Tree, RegexpChunkParser
from nltk.chunk import RegexpParser
from nltk.chunk.regexp import ChunkString, ChunkRule, ChinkRule

s = [('the', 'DT'), ('book', 'NN'), ('has', 'VBZ'), ('many', 'JJ'), ('chapters', 'NNS')]
# forth
chunker = RegexpParser(r'''
NP:
    {<DT><NN.*><.*>*<NN.*>}
    }<VB.*>{'''
)

print(chunker.parse(s))

# back
t = Tree('S', s)
cs = ChunkString(t)
print(cs)

ur = ChunkRule('<DT><NN.*><.*>*<NN.*>', 'chunk determiners and nouns')
ur.apply(cs)
print(cs)

ir = ChinkRule('<VB.*>', 'chink verbs')
ir.apply(cs)
print(cs)

print(cs.to_chunkstruct())
# cs.to_chunkstruct().draw()

chunker = RegexpChunkParser([ur, ir])
print(chunker.parse(t))

# set chunk name
chunker = RegexpChunkParser([ur, ir], chunk_label='CP')
print(chunker.parse(t))

# alternative patterns
chunker1 = RegexpParser(r'''
NP:
    {<DT><NN.*>}
    {<JJ><NN.*>}'''
)
print(chunker1.parse(s))

chunker2 = RegexpParser(r'''
NP:
    {(<DT>|<JJ>)<NN.*>}'''
)
print(chunker2.parse(s))

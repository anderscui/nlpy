from nltk.corpus.reader import ChunkedCorpusReader
from nltk.tokenize import SpaceTokenizer
import nltk

d = nltk.data.find('corpora/cookbook')
reader = ChunkedCorpusReader(d, r'.*\.chunk')
print(reader.chunked_words())
print(reader.chunked_sents())
print(reader.chunked_paras())

# reader.chunked_sents()[0].draw()
print(reader.chunked_sents()[0].leaves())

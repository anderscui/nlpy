from nltk.corpus.util import LazyCorpusLoader
from nltk.corpus.reader import WordListCorpusReader

reader = LazyCorpusLoader('cookbook', WordListCorpusReader, ['wordlist.txt'])
print(isinstance(reader, LazyCorpusLoader))

print(reader.fileids())
print(isinstance(reader, LazyCorpusLoader))
print(isinstance(reader, WordListCorpusReader))

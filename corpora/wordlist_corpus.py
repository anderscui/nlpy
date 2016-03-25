from nltk.corpus.reader import WordListCorpusReader
import nltk

# print(nltk.data.find('corpora/cookbook'))
# print(nltk.data.find('corpora/cookbook/wordlist.txt'))

d = nltk.data.find('corpora/cookbook')
reader = WordListCorpusReader(d, ['wordlist.txt'])
print(reader.words())
print(reader.fileids())

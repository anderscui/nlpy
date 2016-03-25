from nltk.corpus.reader import CategorizedPlaintextCorpusReader
import nltk

d = nltk.data.find('corpora/cookbook')
reader = CategorizedPlaintextCorpusReader(d, r'movie_.*\.txt', cat_pattern=r'movie_(\w+)\.txt')
print(reader.categories())
print(reader.fileids(categories='neg'))
print(reader.fileids(categories='pos'))

# from nltk.corpus import brown
# print(brown.categories())

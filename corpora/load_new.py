from nltk.corpus import PlaintextCorpusReader

corpus_root = '.'
word_lists = PlaintextCorpusReader(corpus_root, '.*\.txt')
print(word_lists.fileids())
print(word_lists.words('phone_says.txt'))
print(word_lists.words('books_cn.txt'))

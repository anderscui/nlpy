from nltk import bigrams

b = list(bigrams(['more', 'is', 'said', 'than', 'done']))
print(b)

from common.books import text4, text8

print(text4().collocations())
print(text8().collocations())
from nltk.book import text4

from common.utils import lexical_diversity

## How we represent text in Python - lists
sent1 = ['Call', 'me', 'Ishmael', '.']

print(sent1)
print(len(sent1))
print(lexical_diversity(sent1))

## indexing
print("the 173rd token is {0}".format(text4[173]))
print("index of 'awaken' is {0}".format(text4.index('awaken')))


##

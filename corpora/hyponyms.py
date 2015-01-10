import nltk
from nltk.corpus import wordnet as wn

motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
print(sorted([lemma.name()
              for synset in types_of_motorcar
              for lemma in synset.lemmas()]))

nltk.app.wordnet()
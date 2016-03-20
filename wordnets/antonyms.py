from nltk.corpus import wordnet

gn2 = wordnet.synset('good.n.02')
print(gn2.definition())

evil = gn2.lemmas()[0].antonyms()[0]
print(evil.name())
print(evil.synset().definition())

from nltk.corpus import wordnet

syn = wordnet.synsets('cookbook')[0]
lemmas = syn.lemmas()
print(len(lemmas))
print(lemmas[0].name())
print(lemmas[1].name())
print(lemmas[0].synset() == lemmas[1].synset())

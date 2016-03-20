from nltk.corpus import wordnet

syn = wordnet.synsets('cookbook')[0]
print(syn.name())
print(syn.definition())

# examples
print(wordnet.synsets('cooking')[0].examples())

# hypernym and hyponym
print(syn.hypernyms())
print(syn.hypernyms()[0].hyponyms())
print(syn.root_hypernyms())

# hypernym paths
print(syn.hypernym_paths())

# POS
print(syn.pos())

print(len(wordnet.synsets('great')))
print(len(wordnet.synsets('great', pos='n')))
print(len(wordnet.synsets('great', pos='a')))

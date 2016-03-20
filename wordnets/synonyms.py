from nltk.corpus import wordnet

synonyms = []
for syn in wordnet.synsets('book'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
print(len(synonyms))
print(len(set(synonyms)))

print(set(synonyms))

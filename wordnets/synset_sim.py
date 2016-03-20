from nltk.corpus import wordnet

cb = wordnet.synset('cookbook.n.01')
ib = wordnet.synset('instruction_book.n.01')
print(cb.wup_similarity(ib))

# shortest path dist
ref = cb.hypernyms()[0]
print(cb.shortest_path_distance(ref))
print(ib.shortest_path_distance(ref))
print(cb.shortest_path_distance(ib))

# dissimilar words
dog = wordnet.synset('dog')[0]
print(dog.wup_similarity(cb))
# print(sorted(dog.common_hypernyms(cb)))


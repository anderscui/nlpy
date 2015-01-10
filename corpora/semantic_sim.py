from nltk.corpus import wordnet as wn

right = wn.synset('right_whale.n.01')
tortoise = wn.synset('tortoise.n.01')
novel = wn.synset('novel.n.01')

print(right.lowest_common_hypernyms(tortoise))
# [Synset('vertebrate.n.01')]
print(right.lowest_common_hypernyms(novel))
# [Synset('entity.n.01')]


print(wn.synset('monkey.n.01')).min_depth()
# 12
print(wn.synset('vertebrate.n.01')).min_depth()
# 8
print(wn.synset('entity.n.01')).min_depth()
# 0
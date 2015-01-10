from nltk.corpus import wordnet as wn
print(wn.synsets('motorcar'))
#[Synset('car.n.01')]
print(wn.synset('car.n.01').definition())
#a motor vehicle with four wheels; usually propelled by an internal combustion engine
print(wn.synset('car.n.01').examples())
#[u'he needs a car to get to work']

print(wn.synset('car.n.01').lemmas())
print(wn.lemmas('car'))

print(wn.lemmas('dish'))
# [Lemma('dish.n.01.dish'), Lemma('dish.n.02.dish'), Lemma('dish.n.03.dish'), Lemma('smasher.n.02.dish'), Lemma('dish.n.05.dish'), Lemma('cup_of_tea.n.01.dish'), Lemma('serve.v.06.dish'), Lemma('dish.v.02.dish')]
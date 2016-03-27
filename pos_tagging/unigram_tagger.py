from nltk.tag import UnigramTagger
from nltk.corpus import treebank

# train
train_sents = treebank.tagged_sents()[:3000]
tagger = UnigramTagger(train_sents)

print(treebank.sents()[0])
print(tagger.tag(treebank.sents()[0]))

# test
test_sents = treebank.tagged_sents()[3000:]
print(tagger.evaluate(test_sents))


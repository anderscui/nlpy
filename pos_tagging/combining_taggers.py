from nltk.tag import UnigramTagger, DefaultTagger
from nltk.corpus import treebank

# train
default_tagger = DefaultTagger('NN')

train_sents = treebank.tagged_sents()[:3000]
tagger = UnigramTagger(train_sents, backoff=default_tagger)

# test
test_sents = treebank.tagged_sents()[3000:]
print(tagger.evaluate(test_sents))

# save to pickle
import pickle
with open('unitagger.pkl', 'wb') as output:
    pickle.dump(tagger, output)

# load from pickle
with open('unitagger.pkl', 'rb') as data_file:
    tagger2 = pickle.load(data_file)

print(tagger2.evaluate(test_sents))

# or nltk.data.load('unitagger.pkl') to load

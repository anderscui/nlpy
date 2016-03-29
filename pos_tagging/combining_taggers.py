from nltk.tag import UnigramTagger, DefaultTagger
from nltk.corpus import treebank

from tag_util import train_sents, test_sents

# train
default_tagger = DefaultTagger('NN')
tagger = UnigramTagger(train_sents, backoff=default_tagger)

# test
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

from nltk.tag import DefaultTagger, UnigramTagger, BigramTagger, TrigramTagger
from nltk.corpus import treebank

train_sents = treebank.tagged_sents()[:3000]
test_sents = treebank.tagged_sents()[3000:]

bitagger = BigramTagger(train_sents)
print(bitagger.evaluate(test_sents))

tritagger = TrigramTagger(train_sents)
print(tritagger.evaluate(test_sents))


def backoff_tagger(train_sents, tagger_classes, backoff=None):
    combined = backoff
    for cls in tagger_classes:
        combined = cls(train_sents, backoff=combined)
    return combined

default_tagger = DefaultTagger('NN')
combined_tagger = backoff_tagger(train_sents, [UnigramTagger, BigramTagger, TrigramTagger], backoff=default_tagger)
print(combined_tagger.evaluate(test_sents))

# # train
# default_tagger = DefaultTagger('NN')
#
# train_sents = treebank.tagged_sents()[:3000]
# tagger = UnigramTagger(train_sents, backoff=default_tagger)
#
# # test
# test_sents = treebank.tagged_sents()[3000:]
# print(tagger.evaluate(test_sents))
#
# # save to pickle
# import pickle
# with open('unitagger.pkl', 'wb') as output:
#     pickle.dump(tagger, output)
#
# # load from pickle
# with open('unitagger.pkl', 'rb') as data_file:
#     tagger2 = pickle.load(data_file)
#
# print(tagger2.evaluate(test_sents))
#
# # or nltk.data.load('unitagger.pkl') to load

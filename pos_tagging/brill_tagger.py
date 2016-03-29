from nltk import DefaultTagger, UnigramTagger, BigramTagger, TrigramTagger
from tag_util import backoff_tagger, train_sents, test_sents, train_brill_tagger

default_tagger = DefaultTagger('NN')
init_tagger = backoff_tagger(train_sents, [UnigramTagger, BigramTagger, TrigramTagger], backoff=default_tagger)
print(init_tagger.evaluate(test_sents))

brill_tagger = train_brill_tagger(init_tagger, train_sents)
print(brill_tagger.evaluate(test_sents))

from nltk.tag import UnigramTagger, BigramTagger, TrigramTagger, DefaultTagger
from tag_util import backoff_tagger, train_sents, test_sents
from taggers import WordNetTagger

de_tagger = DefaultTagger('NN')
wn_tagger = WordNetTagger(backoff=de_tagger)
tagger = backoff_tagger(train_sents, [UnigramTagger, BigramTagger, TrigramTagger], backoff=wn_tagger)
print(tagger.evaluate(test_sents))

from nltk.tag import RegexpTagger
from tag_util import patterns, test_sents


tagger = RegexpTagger(patterns)
print(tagger.evaluate(test_sents))

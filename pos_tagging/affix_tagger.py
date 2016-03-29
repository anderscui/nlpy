from nltk.tag import AffixTagger
from tag_util import train_sents, test_sents

tagger = AffixTagger(train_sents)
print(tagger.evaluate(test_sents))

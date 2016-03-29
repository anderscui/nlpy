from nltk.tag.sequential import ClassifierBasedPOSTagger
from tag_util import train_sents, test_sents

tagger = ClassifierBasedPOSTagger(train=train_sents)
print(tagger.evaluate(test_sents))

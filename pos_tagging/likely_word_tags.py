from nltk import UnigramTagger
from nltk.corpus import treebank

from tag_util import word_tag_model

model = word_tag_model(treebank.words(), treebank.tagged_words())
tagger = UnigramTagger(model=model)

test_sents = treebank.tagged_sents()[3000:]
print(tagger.evaluate(test_sents))

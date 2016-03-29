from nltk.tag import tnt, RegexpTagger, DefaultTagger
from tag_util import train_sents, test_sents, patterns

tnt_tagger = tnt.TnT()
tnt_tagger.train(train_sents)
print(tnt_tagger.evaluate(test_sents))
# 0.875631340384

# deal with unknown tokens
default_tagger = DefaultTagger('NN')
unk_tagger = RegexpTagger(patterns, backoff=default_tagger)

tnt_tagger2 = tnt.TnT(unk=unk_tagger, Trained=True)
tnt_tagger2.train(train_sents)
print(tnt_tagger2.evaluate(test_sents))
# 0.896956615584

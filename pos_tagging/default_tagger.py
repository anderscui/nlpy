# every tagger has a tag() method.
# DefaultTagger is a subclass of SequentialBackoffTagger which has a choose_tag() method.
from nltk.tag import DefaultTagger
from nltk.corpus import treebank

tagger = DefaultTagger('NN')
print(tagger.tag(['Hello', 'World']))

# thought it's too simple, we can try to evaluate it
test_sents = treebank.tagged_sents()[3000:]
print(tagger.evaluate(test_sents))

# for sentences
print(tagger.tag_sents([['Hello', 'World', '.'], ['How', 'are', 'you', '?']]))

# untagging
from nltk.tag import untag

print(untag([('Hello', 'NN'), ('World', 'NN')]))

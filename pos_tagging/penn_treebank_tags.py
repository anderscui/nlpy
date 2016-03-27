from nltk.probability import FreqDist
from nltk.corpus import treebank

fd = FreqDist()
for word, tag in treebank.tagged_words():
    fd[tag] += 1
tags = list(fd.items())
tags.sort(key=lambda (tag, freq): tag)
for tag, freq in tags:
    print('{0}\t\t\t{1}'.format(tag, freq))

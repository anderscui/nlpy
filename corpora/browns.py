from nltk.corpus import brown

print(brown.categories())

print(brown.words(categories='news'))
print(brown.words(fileids=['cg22']))
print(brown.sents(categories=['news', 'editorial', 'reviews']))

from nltk import FreqDist
news = brown.words(categories='news')
fdist = FreqDist([w.lower() for w in news])
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print('{0}: {1}'.format(m, fdist[m]))
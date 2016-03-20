from nltk.corpus import webtext
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

words = [w.lower() for w in webtext.words('grail.txt')]
bcf = BigramCollocationFinder.from_words(words)
print(bcf.nbest(BigramAssocMeasures.likelihood_ratio, 4))

# remove punctuation and stopwords
from nltk.corpus import stopwords

stopset = set(stopwords.words('english'))
filter_stops = lambda w: len(w) < 3 or w in stopset
bcf.apply_word_filter(filter_stops)
print(bcf.nbest(BigramAssocMeasures.likelihood_ratio, 4))

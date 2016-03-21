from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('cooking'))
print(lemmatizer.lemmatize('cooking', pos='v'))
print(lemmatizer.lemmatize('cooking', pos='n'))
print(lemmatizer.lemmatize('cookbooks'))

# vs. stemming
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
print(stemmer.stem('beleives'))
print(lemmatizer.lemmatize('believes'))

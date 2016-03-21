from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, RegexpStemmer
from nltk.stem.snowball import EnglishStemmer

stemmer = PorterStemmer()
print(stemmer.stem('cooking'))
print(stemmer.stem('cookery'))

stemmer2 = LancasterStemmer()
print(stemmer2.stem('cooking'))
print(stemmer2.stem('cookery'))

stemmer3 = SnowballStemmer('english')
print(stemmer3.stem('cooking'))
print(stemmer3.stem('cookery'))

# english is also Porter.
stemmer_en = EnglishStemmer()
print(stemmer_en.stem('cooking'))
print(stemmer_en.stem('cookery'))

# regex
stemmer_reg = RegexpStemmer('ing')
print(stemmer_reg.stem('cooking'))
print(stemmer_reg.stem('thing'))

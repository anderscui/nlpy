from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

tokenizer = RegexpTokenizer('\s+', gaps=True)
english_stopwords = set(stopwords.words('english'))
words = tokenizer.tokenize("Can't is a contraction.")
print(words)
filtered = [word for word in words if word not in english_stopwords]
print(filtered)

# stopwords of all languages
# print(stopwords.words())

# languages
print(stopwords.fileids())

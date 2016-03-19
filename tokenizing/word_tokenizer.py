from nltk.tokenize import word_tokenize

print(word_tokenize('Hello NLTK.'))

# or
from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
print(tokenizer.tokenize('Hello NLTK.'))

# note the contractions
print(tokenizer.tokenize("can't"))

from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer("[\w']+")
print(tokenizer.tokenize("Can't is a contraction."))

# or
from nltk.tokenize import regexp_tokenize
print(regexp_tokenize("Can't is a contraction.", "[\w']+"))

# use gaps
tokenizer = RegexpTokenizer('\s+', gaps=True)
print(tokenizer.tokenize("Can't is a contraction."))

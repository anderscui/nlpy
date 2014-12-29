from nltk.book import text3, text4, text5

from common.utils import lexical_diversity, percentage


## counting tokens (words and punctuations) - 44764
# print(len(text3))

## counting unique tokens - 2789

dict3 = sorted(set(text3))
print(dict3[1:50])
print(len(dict3))

## lexical diversity
print("tokens: {0}, types: {1}, lexical diversity: {2}".format(len(text3), len(dict3), lexical_diversity(text3)))

## word frequency
print("text3 has {0} word '{1}'".format(text3.count('smote'), 'smote'))
print("percentage of 'a' in text4 is {0}".format(percentage(text4.count('a'), len(text4))))


print("text5 (Chat Corpus) has {0} word '{1}'".format(text5.count('lol'), 'lol'))
print("percentage of 'lol' in text5 is {0}".format(percentage(text5.count('lol'), len(text5))))
from nltk import FreqDist
from common.books import text1

fdist = FreqDist(len(w) for w in text1())
print(fdist)
# print(fdist.keys())
# print(fdist.items())

print(fdist.most_common())
print(fdist.max())
print(fdist[3])
print(fdist.freq(3))

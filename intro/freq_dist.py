from nltk import FreqDist

from common.books import text1

t1 = text1()
fdist1 = FreqDist(t1)
print(fdist1)
print("moby dick has {0} words, {1} unique ones.".format(fdist1.N(), fdist1.B()))

voc1 = fdist1.keys()
# the type is dict_keys
# print(type(voc1))

# change back to a normal list
# voc1 = list(voc1)
# print(voc1[:50])

# i = 0
# for k in voc1:
#     if i < 50:
#         print(k)
#         i += 1
#     else:
#         break

print(fdist1.most_common(50))

print("'whale' has {0} occurences.".format(fdist1['whale']))

fdist1.plot(50, cumulative=True)

## to get the topic of a book/article, neither frequent nor infrequent words help.

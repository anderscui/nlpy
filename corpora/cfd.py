from nltk import ConditionalFreqDist
from nltk.corpus import brown

# cfd = ConditionalFreqDist(
#     (genre, word)
#     for genre in brown.categories()
#     for word in brown.words(categories=genre)
# )
# print(len(cfd))  # 15 (categories)

cfd = ConditionalFreqDist(
    (genre, word)
    for genre in ['news', 'romance']
    for word in brown.words(categories=genre)
)
print(cfd)  # 2 (categories)
print(cfd.conditions())
print(cfd['romance'])  # FreqDist with 8452 samples and 70022 outcomes

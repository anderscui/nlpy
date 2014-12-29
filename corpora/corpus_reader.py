import nltk
from nltk.corpus import gutenberg

emma = gutenberg.words('austen-emma.txt')
print(len(emma))

emma = nltk.Text(gutenberg.words('austen-emma.txt'))
print(emma.concordance('surprize'))

# raw = gutenberg.raw("burgess-busterbrown.txt")
# print(raw[1:20])

# words
# words = gutenberg.words("burgess-busterbrown.txt")
# print(words[1:20])

# sents = gutenberg.sents("burgess-busterbrown.txt")
# print(sents[1:20])

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))

    print(round(num_chars / num_words), round(num_words / num_sents), round(num_words / num_vocab), fileid)
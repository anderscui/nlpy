STOP_WORDS = {"the", "of", "is", "and", "to", "in", "that", "we", "for", "an", "are", "by", "be", "as", "on", "with",
              "can", "if", "from", "which", "you", "it", "this", "then", "at", "have", "all", "not", "one", "has", "or",
              "that"}

d = {
    'the': 5,
    'of': 8,
    'is': 6
}

from operator import itemgetter
print(sorted(d.items(), key=itemgetter(1), reverse=True))
print(sorted(d, key=d.__getitem__, reverse=True))
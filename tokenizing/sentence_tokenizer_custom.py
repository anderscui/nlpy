from nltk.tokenize import sent_tokenize

para = """White guy: So, do you have any plans for this evening?
Asian girl: Yeah, being angry!
White guy: Oh, that sounds good.

Guy #1: So this Jack guy is basically the luckiest man in the world."""
# print(sent_tokenize(para))

# read full overheard.txt corpus
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import webtext

text = webtext.raw('overheard.txt')
sent_tokenizer = PunktSentenceTokenizer(text)

sents1 = sent_tokenizer.tokenize(text)
sents2 = sent_tokenize(text)

print(sents1[0])
print(sents2[0])

print(sents1[678])
print(sents2[678])

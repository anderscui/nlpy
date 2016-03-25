from nltk.corpus.reader import TaggedCorpusReader
from nltk.tokenize import SpaceTokenizer
import nltk

d = nltk.data.find('corpora/cookbook')
reader = TaggedCorpusReader(d, r'.*\.pos')
print(reader.words())
print(reader.tagged_words())
print(reader.sents())
print(reader.tagged_sents())
print(reader.paras())
print(reader.tagged_paras())

# custom tokenizer
reader = TaggedCorpusReader(d, r'.*\.pos', word_tokenizer=SpaceTokenizer())
print(reader.sents())
print(reader.tagged_sents())

# universal tagset
reader = TaggedCorpusReader(d, r'.*\.pos', word_tokenizer=SpaceTokenizer(), tagset='en-brown')
print(reader.tagged_sents(tagset='universal'))

# NLTK tagged corpora
from nltk.corpus import treebank
print(reader.tagged_words())
print(reader.tagged_words(tagset='universal'))

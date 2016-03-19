from nltk.tokenize import sent_tokenize

para = "Hello world. It's good to see you. Thanks for giving me this. I will go to U.S.A. next week."
print(sent_tokenize(para))

# load once, use many times
import nltk.data
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
print(tokenizer.tokenize(para))

# other languages
tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')
para = 'Hola amigo. Estoy bien.'
print(tokenizer.tokenize(para))

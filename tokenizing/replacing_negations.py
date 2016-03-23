from nltk.tokenize import word_tokenize
from replacers import AntonymReplacer

replacer = AntonymReplacer()

sent = "let's not uglify our code"
print(replacer.replace_negations(word_tokenize(sent)))

print(replacer.replace_negations(word_tokenize("it is not small")))
print(replacer.replace_negations(word_tokenize("it is not high")))
print(replacer.replace_negations(word_tokenize("it is not fine")))

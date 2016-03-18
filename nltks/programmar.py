import nltk

# int i = 0
# var j = 1:5
grammar1 = nltk.data.load('file:programmar.cfg')
sent = 'int i = 0'.split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)

sent = 'say()'.split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)

sent = 'var j = val()'.split()
rd_parser = nltk.RecursiveDescentParser(grammar1, trace=1)
for tree in rd_parser.parse(sent):
    print(tree)

import nltk

grammar1 = nltk.data.load('file:mygrammar.cfg')
sent = 'Mary saw Bob'.split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)

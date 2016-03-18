import nltk
from nltk.corpus import treebank

# show samples of treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]
# print(t)

# filter sentential complements
def filter(tree):
    child_nodes = [child.label() for child in tree if isinstance(child, nltk.Tree)]
    return (tree.label() == 'VP') and ('S' in child_nodes)


subtrees = [subtree for tree in treebank.parsed_sents()
            for subtree in tree.subtrees(filter)]
for st in subtrees:
    print(st)

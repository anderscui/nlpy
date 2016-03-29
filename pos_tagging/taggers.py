from nltk import FreqDist
from nltk.tag import SequentialBackoffTagger
from nltk.corpus import names, wordnet


class WordNetTagger(SequentialBackoffTagger):

    def __init__(self, *args, **kwargs):
        SequentialBackoffTagger.__init__(self, *args, **kwargs)

        self.wordnet_tag_map = {
            'n': 'NN',
            's': 'JJ',
            'a': 'JJ',
            'r': 'RB',
            'v': 'VB'
        }

    def choose_tag(self, tokens, index, history):
        word = tokens[index]
        fd = FreqDist()

        for synset in wordnet.synsets(word):
            fd[synset.pos()] += 1

        if fd:
            return self.wordnet_tag_map.get(fd.max())
        else:
            return None


class NamesTagger(SequentialBackoffTagger):
    def __init__(self, *args, **kwargs):
        SequentialBackoffTagger.__init__(self, *args, **kwargs)
        self.name_set = set([n.lower() for n in names.words()])

    def choose_tag(self, tokens, index, history):
        word = tokens[index]
        if word.lower() in self.name_set:
            return 'NNP'
        else:
            return None

from nltk.corpus import treebank
from nltk.probability import FreqDist, ConditionalFreqDist
from nltk.tag import brill, brill_trainer

patterns = [
    (r'^\d+$', 'CD'),
    (r'.*ing$', 'VBG'),  # gerunds
    (r'.*ment$', 'NN'),  # movement
    (r'.*ful$', 'JJ'),  # wonderful
]


def backoff_tagger(train_sents, tagger_classes, backoff=None):
    combined = backoff
    for cls in tagger_classes:
        combined = cls(train_sents, backoff=combined)
    return combined


def word_tag_model(words, tagged_words, limit=200):
    fd = FreqDist(words)
    cfd = ConditionalFreqDist(tagged_words)
    most_freq = (word for word, count in fd.most_common(limit))
    return dict((word, cfd[word].max()) for word in most_freq)


def train_brill_tagger(initial_tagger, train_sents, **kwargs):
    templates = [
        brill.Template(brill.Pos([-1])),
        brill.Template(brill.Pos([1])),
        brill.Template(brill.Pos([-2])),
        brill.Template(brill.Pos([2])),
        brill.Template(brill.Pos([-2, -1])),
        brill.Template(brill.Pos([1, 2])),
        brill.Template(brill.Pos([-3, -2, -1])),
        brill.Template(brill.Pos([1, 2, 3])),
        brill.Template(brill.Pos([-1]), brill.Pos([1])),
        brill.Template(brill.Word([-1])),
        brill.Template(brill.Word([1])),
        brill.Template(brill.Word([-2])),
        brill.Template(brill.Word([2])),
        brill.Template(brill.Word([-2, -1])),
        brill.Template(brill.Word([1, 2])),
        brill.Template(brill.Word([-3, -2, -1])),
        brill.Template(brill.Word([1, 2, 3])),
        brill.Template(brill.Word([-1]), brill.Word([1])),
    ]

    trainer = brill_trainer.BrillTaggerTrainer(initial_tagger, templates, deterministic=True)
    return trainer.train(train_sents, **kwargs)


train_sents = treebank.tagged_sents()[:3000]
test_sents = treebank.tagged_sents()[3000:]

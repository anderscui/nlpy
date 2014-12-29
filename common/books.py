from nltk import Text
from nltk.corpus import gutenberg, genesis, webtext, inaugural


def text1():
    text = Text(gutenberg.words('melville-moby_dick.txt'))
    print("text1:", text.name)
    return text


def moby_dick():
    return text1()


def text2():
    text = Text(gutenberg.words('austen-sense.txt'))
    print("text2:", text.name)
    return text


def text3():
    text = Text(genesis.words('english-kjv.txt'), name="The Book of Genesis")
    print("text3:", text.name)
    return text


def text4():
    text = Text(inaugural.words(), name="Inaugural Address Corpus")
    print("text4:", text.name)
    return text


def text8():
    text = Text(webtext.words('singles.txt'), name="Personals Corpus")
    print("text8:", text.name)
    return text
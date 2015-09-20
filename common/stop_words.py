# coding=utf-8
from nltk.corpus import stopwords
from common.chinese import read_lines


def english():
    return stopwords.words('english')


def chinese():
    return set([line.strip() for line in read_lines('../dicts/data/stopwords_zh.txt')])


if __name__ == '__main__':
    sw = chinese()
    for w in sw[50:60]:
        print(w)

    assert u'不仅' in sw
    assert u',' in sw
    assert u'，' in sw
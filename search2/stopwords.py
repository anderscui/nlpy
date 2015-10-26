# coding=utf-8
from common.chinese import read_lines
from common.persistence import to_pickle


def chinese():
    hit = set([line.strip() for line in read_lines('stopwords_zh.txt')])
    lagou = set([line.strip() for line in read_lines('stopwords_lagou.txt')])
    en = set([line.strip() for line in read_lines('stopwords_en.txt')])

    return en | hit | lagou


if __name__ == '__main__':
    stopwords = chinese()
    to_pickle(stopwords, 'stopwords.pkl')
    print 'he' in stopwords
    print u'he' in stopwords

    print u'他' in stopwords
    print u'职位' in stopwords
    print u'负责' in stopwords
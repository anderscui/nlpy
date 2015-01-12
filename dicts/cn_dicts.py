from collections import defaultdict
from common import chinese
from common.persistence import to_pickle, from_pickle


def is_comment(s):
    return s.startswith('#')


def save_chinese_stopwords():
    dict_file = './data/stopwords_zh_hit.txt'
    lines = chinese.read_lines(dict_file)
    dict_data = [w.strip() for w in lines if w.strip()]
    to_pickle(dict_data, './data/stopwords_zh.pkl')


def load_stopwords(lan='chinese'):
    if lan == 'chinese':
        dict_data = from_pickle('./data/stopwords_zh.pkl')
        return dict_data


def save_pos_sentiment_dict():
    dict_file = './data/pos_sent_zh.txt'
    lines = chinese.read_lines(dict_file)
    dict_data = [w.strip() for w in lines if w.strip()]
    to_pickle(dict_data, './data/pos_sent_zh.pkl')


def load_pos_sentiment_dict(lan='chinese'):
    if lan == 'chinese':
        dict_data = from_pickle('./data/pos_sent_zh.pkl')
        return dict_data


def save_neg_sentiment_dict():
    dict_file = './data/neg_sent_zh.txt'
    lines = chinese.read_lines(dict_file)
    dict_data = [w.strip() for w in lines if w.strip()]
    to_pickle(dict_data, './data/neg_sent_zh.pkl')


def save_degree_dict():
    dict_file = './data/degree_zh.txt'
    lines = chinese.read_lines(dict_file)

    degree = 0
    degree_dict = defaultdict(int)
    for l in lines:
        l = l.strip()

        if l and (not is_comment(l)):
            if l[0].isdigit():
                parts = l.split('-')
                assert len(parts) == 2
                degree = int(parts[1])
            else:
                degree_dict[l] = degree

    for k in degree_dict:
        print(k, degree_dict[k])

    to_pickle(degree_dict, './data/degree_zh.pkl')


def save_inverse_dict():
    dict_file = './data/inverse_zh.txt'
    lines = chinese.read_lines(dict_file)

    inv_dict = [w.strip() for w in lines if w.strip() and (not is_comment(w))]
    to_pickle(inv_dict, './data/inverse_zh.pkl')


if __name__ == '__main__':
    # save_chinese_stopwords()
    # stopwords = load_stopwords()
    # for w in stopwords[10:20]:
    #     print(w)

    # save_pos_sentiment_dict()
    # pos_sent = load_pos_sentiment_dict()
    # for w in pos_sent[:10]:
    #     print(w)

    # save_neg_sentiment_dict()
    # save_degree_dict()

    save_inverse_dict()

    # file_path
    # print(__file__)
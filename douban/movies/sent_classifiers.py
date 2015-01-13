# coding=utf-8
import jieba
from common.persistence import from_pickle, to_pickle


def clear_non_sentiments():
    all_reviews = from_pickle('./all_reviews.pkl')
    print(len(all_reviews))

    has_sentiment = [(score, review) for (score, review) in all_reviews if score > 0 and len(review) > 0]
    to_pickle(has_sentiment, './sent_reviews.pkl')
    print(len(has_sentiment))

    to_pickle(has_sentiment[:10000], './train0.pkl')


def load_small():
    return from_pickle('./train0.pkl')


def load_pos_words():
    return from_pickle('./dicts/pos_sent_zh.pkl')


def load_neg_words():
    return from_pickle('./dicts/neg_sent_zh.pkl')


def load_inv_dict():
    return from_pickle('./dicts/inverse_zh.pkl')


def load_degree_words():
    return from_pickle('./dicts/degree_zh.pkl')


def load_stopwords():
    return from_pickle('./dicts/stopwords_zh.pkl')


stopwords = load_stopwords()

# 碾压；五星；四星；二星，一星；想给你生孩子；过誉；艹；混蛋；木有；


if __name__ == '__main__':
    # clear_non_sentiments()

    # small data
    reviews = load_small()

    rating = [r[0] for r in reviews if r[0] != 3]
    comments = [r[1] for r in reviews if r[0] != 3]
    assert len(rating) == len(comments)
    print(len(rating))

    cnt = 50
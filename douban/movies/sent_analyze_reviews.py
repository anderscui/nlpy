# coding=utf-8

import numpy as np

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


def is_even(n):
    return (n % 2) == 0


pos_words = load_pos_words()
neg_words = load_neg_words()
inv_dict = load_inv_dict()
degree_words = load_degree_words()
stopwords = load_stopwords()

degrees = [12, 29, 30, 37, 42, 69]
dweights = [0.25, 0.5, 1.0, 2.0, 3.0, 4.0]


def degree_weight(degree):
    w = 1.0
    try:
        i = degrees.index(degree)
    except ValueError:
        # print(degree)
        # print('degree not found')
        i = -1
    if i >= 0:
        w = dweights[i]

    return w


def cut_sentence(words):
    # words = (words).decode('utf8')
    start = 0
    i = 0
    sents = []
    punt_list = ',.!?:;~，。！？：；～'.decode('utf8')
    token = None
    for word in words:
        if word in punt_list and token not in punt_list:  # 检查标点符号下一个字符是否还是标点
            sents.append(words[start:i + 1])
            start = i + 1
            i += 1
        else:
            i += 1
            token = list(words[start:i + 2]).pop()  # 取下一个字符
    if start < len(words):
        sents.append(words[start:])
    return sents


def segmentation(sentence, para):
    if para == 'str':
        seg_list = jieba.cut(sentence)
        seg_result = ' '.join(seg_list)
        return seg_result
    elif para == 'list':
        seg_list2 = jieba.cut(sentence)
        seg_result2 = []
        for w in seg_list2:
            seg_result2.append(w)
        return seg_result2


def sent_scores(data):
    review_score = []
    all_scores = []

    for sents in data:
        for sent in sents:
            segtmp = segmentation(sent, 'list')

            i = 0  # 记录扫描到的词的位置
            a = 0  # 记录情感词的位置

            pos_score = 0
            neg_score = 0

            for word in segtmp:
                # print(word)
                if word in pos_words:
                    # print('+' + word)
                    cur_pos_score = 1
                    for w in segtmp[a:i]:
                        if w in degree_words:
                            # print('*' + w)
                            cur_pos_score *= degree_weight(degree_words[w])
                        elif w in inv_dict:
                            # print('!' + w)
                            cur_pos_score *= -1

                    if cur_pos_score < 0:
                        neg_score += (-cur_pos_score)
                    else:
                        pos_score += cur_pos_score

                    a = i + 1
                elif word in neg_words:
                    # print('-' + word)
                    cur_neg_score = 1
                    for w in segtmp[a:i]:
                        if w in degree_words:
                            # print('*' + w)
                            cur_neg_score *= degree_weight(degree_weight(w))
                        elif w in inv_dict:
                            # print('!' + w)
                            cur_neg_score *= -1

                    if cur_neg_score < 0:
                        pos_score += (-cur_neg_score)
                    else:
                        neg_score += cur_neg_score

                    a = i + 1
                elif word == '！'.decode('utf8') or word == '!'.decode('utf8'):
                    for w2 in segtmp[::-1]:  # 扫描感叹号前的情感词
                        if w2 in pos_words:
                            pos_score += 2
                            break
                        elif w2 in neg_words:
                            neg_score += 2
                            break
                i += 1

            review_score.append([pos_score, neg_score])
        all_scores.append(review_score)
        review_score = []

    return all_scores


def final_sentiments(scores):
    final = []
    for s in scores:
        sa = np.array(s)
        pos = np.sum(sa[:, 0])
        neg = np.sum(sa[:, 1])
        pos_avg = np.mean(sa[:, 0])
        neg_avg = np.mean(sa[:, 1])
        total = pos_avg - neg_avg
        pos_std = np.std(sa[:, 0])
        neg_std = np.std(sa[:, 1])

        final.append([pos, neg, pos_avg, neg_avg, pos_std, neg_std, total])

    return final


# 碾压；五星；四星；二星，一星；想给你生孩子；过誉；艹；混蛋；木有；

def stars_to_sentiments(s):
    if s > 3:
        return 1
    elif s == 3:
        return 0
    else:
        return -1


def score_to_sentiments(s):
    if s > 0:
        return 1
    elif s < 0:
        return -1
    else:
        return 0


if __name__ == '__main__':
    # clear_non_sentiments()

    # small data
    reviews = load_small()
    assert len(reviews) == 10000
    # for r in reviews[:10]:
    # print(r[0])
    # print(r[1])

    rating = [r[0] for r in reviews]
    sentiments = [stars_to_sentiments(r) for r in rating]
    comments = [r[1] for r in reviews]
    assert len(rating) == len(comments)
    # print(len(rating))

    start = 0
    end = 2000
    sents_cmts = [cut_sentence(c) for c in comments[start:end]]
    scores = sent_scores(sents_cmts)
    final_scores = final_sentiments(scores)
    total_scores = [score_to_sentiments(fs[6]) for fs in final_scores]

    total = len(scores)
    diff = 0
    for i, s in enumerate(scores):
        # print(total_scores[i], sentiments[i])
        if total_scores[i] != sentiments[i]:
            diff += 1
    print(1 - (diff / 500.0))

    # c_comments = [u'很棒',
    #               u'非常好',
    #               u'不失望，也不用强求太多，这就是一种情怀。',
    #               u'剧情靠一边，先爽再说',
    #               u'勉强及格，看得我好累',
    #               u'娱乐大片，难道就不能看。',
    #               u'很爽',
    #               u'1-6都看过，非常刺激！',
    #               u'动作场面挺过瘾的，就是情节弱了点~']
    # sents_cmts = [cut_sentence(c) for c in c_comments]
    # for sents in sents_cmts:
    #     for s in sents:
    #         print(s)
    # scores = sent_scores(sents_cmts)
    # print(scores)
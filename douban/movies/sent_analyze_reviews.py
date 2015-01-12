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
        print('degree not found')
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
            sents.append(words[start:i+1])
            start = i+1
            i += 1
        else:
            i += 1
            token = list(words[start:i+2]).pop()  # 取下一个字符
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

    count1 = []
    count2 = []

    for sents in data:
        for sent in sents:
            segtmp = segmentation(sent, 'list')

            i = 0  #记录扫描到的词的位置
            a = 0  #记录情感词的位置
            poscount = 0  #积极词的第一次分值
            poscount2 = 0  #积极词反转后的分值
            poscount3 = 0  #积极词的最后分值（包括叹号的分值）
            negcount = 0
            negcount2 = 0
            negcount3 = 0

            for word in segtmp:
                if word in pos_words:  # 判断词语是否是情感词
                    print(word)
                    poscount += 1
                    c = 0
                    for w in segtmp[a:i]:  # 扫描情感词前的程度词
                        if w in degree_words:
                            poscount *= degree_weight(degree_words[w])
                        elif w in inv_dict:
                            c += 1
                    if not is_even(c):  # 扫描情感词前的否定词数
                        poscount *= -1.0
                        poscount2 += poscount
                        poscount = 0
                        poscount3 = poscount + poscount2 + poscount3
                        poscount2 = 0
                    else:
                        poscount3 = poscount + poscount2 + poscount3
                        poscount = 0
                    a = i + 1  # 情感词的位置变化
                elif word in neg_words:  # 消极情感的分析，与上面一致
                    print('-' + word)
                    negcount += 1
                    d = 0
                    for w in segtmp[a:i]:
                        if w in degree_words:
                            negcount *= degree_weight(degree_weight(w))
                        elif w in inv_dict:
                            d += 1
                    if not is_even(d):
                        negcount *= -1.0
                        negcount2 += negcount
                        negcount = 0
                        negcount3 = negcount + negcount2 + negcount3
                        negcount2 = 0
                    else:
                        negcount3 = negcount + negcount2 + negcount3
                        negcount = 0
                    a = i + 1
                elif word == '！'.decode('utf8') or word == '!'.decode('utf8'):  # 判断句子是否有感叹号
                    for w2 in segtmp[::-1]:  # 扫描感叹号前的情感词，发现后权值+2，然后退出循环
                        if w2 in pos_words or neg_words:
                            poscount3 += 2
                            negcount3 += 2
                            break
                    i += 1

            #以下是防止出现负数的情况
            pos_count = 0
            neg_count = 0
            if poscount3 < 0 and negcount3 > 0:
                neg_count += negcount3 - poscount3
                pos_count = 0
            elif negcount3 < 0 and poscount3 > 0:
                pos_count = poscount3 - negcount3
                neg_count = 0
            elif poscount3 < 0 and negcount3 < 0:
                neg_count = -poscount3
                pos_count = -negcount3
            else:
                pos_count = poscount3
                neg_count = negcount3

            count1.append([pos_count, neg_count])
        count2.append(count1)
        count1 = []

    return count2


# 碾压；五星；四星；二星，一星；想给你生孩子；过誉；艹；混蛋；


if __name__ == '__main__':
    # clear_non_sentiments()

    # small data
    reviews = load_small()
    assert len(reviews) == 10000
    # for r in reviews[:10]:
    #     print(r[0])
    #     print(r[1])

    rating = [r[0] for r in reviews if r[0] != 3]
    comments = [r[1] for r in reviews if r[0] != 3]
    assert len(rating) == len(comments)
    print(len(rating))

    cnt = 5

    # seg_comments = [jieba.cut(c, cut_all=False) for c in comments[:cnt]]
    # for i, sc in enumerate(seg_comments):
    #     print(comments[i])
    #     print "/ ".join(sc)


    # pos_words = load_pos_words()
    # neg_words = load_neg_words()
    # inv_dict = load_inv_dict()
    # degree_words = load_degree_words()
    # stopwords = load_stopwords()

    # print('pos words')
    # for w in pos_words[:10]:
    #     print(w)

    sents_cmts = [cut_sentence(c) for c in comments[:cnt]]
    # for sents in sents_cmts:
    #     for s in sents:
    #         print(s)
    scores = sent_scores(sents_cmts)
    # print(scores)
    #
    for i, sents in enumerate(sents_cmts):
        for s in sents:
            print(s)
        print(scores[i])
from common.persistence import from_pickle, to_pickle
from common.html_util import strip_tags
from common.stop_words import chinese

pos_dict = from_pickle('pos_norm.pkl')
pid = 403932

pos = pos_dict[pid][2]

import jieba
print pos
# print '/ '.join(jieba.cut(pos))

from nltk.corpus import stopwords

cn_stop_words = chinese()
en_stop_words = stopwords.words('english')
for esw in en_stop_words:
    if esw not in cn_stop_words:
        cn_stop_words.add(esw)
print('stop words: ' + str(len(cn_stop_words)))


def len_one_filter(term):
    return (term == u'r') or (len(term) > 1)


def jieba_tokenize(text):
    # TODO: use set instead of list to filter stop words.
    tokens = jieba.cut(text, cut_all=False)
    return [t.strip() for t in tokens if (not t.isspace()) and len_one_filter(t) and (t.strip() not in cn_stop_words)]


print '/ '.join(jieba_tokenize(pos))


pos_list = []
for pid in pos_dict:
    pos_list.append(jieba_tokenize(pos_dict[pid][2]))


from gensim import corpora, models, similarities
dictionary = corpora.Dictionary(pos_list)
corpus = [dictionary.doc2bow(text) for text in pos_list]
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
# coding=utf-8
from collections import defaultdict
import jieba
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from common.html_util import strip_tags
from common.persistence import from_pickle, to_pickle
from common.stop_words import chinese

job_data_file = '../crawlers/unified.pkl'
jobs = from_pickle(job_data_file)
# print(type(jobs))


skills = [u'Python', u'自然语言处理', u'数据挖掘', u'搜索算法', u'精准推荐', u'用户研究员', u'交互设计师', u'.NET',
          u'Java', u'C', u'PHP', u'Ruby', u'Node.js', u'iOS', u'Android', u'Javascript',
          u'MongoDB', u'产品经理', u'APP设计师', u'UI设计师', u'数据分析师']

jlist = jobs.values()
loaded = defaultdict(list)

for j in jlist:
    if j['skill_tag'] in skills:
        loaded[j['skill_tag']].append(strip_tags(j['desc']))

# print(len(loaded))
# print(len(loaded[u'Python']))
# for desc in loaded[u'Python'][:2]:
#     print(desc)


## start to analyze
cn_stop_words = chinese()
cn_stop_words.append(u'一门')
cn_stop_words.append(u'任一')

en_stop_words = stopwords.words('english')
for esw in en_stop_words:
    if esw not in cn_stop_words:
        cn_stop_words.append(esw)
print('stop words: ' + str(len(cn_stop_words)))


jieba.add_word(u'机器学习', 2000)
jieba.add_word(u'自然语言处理', 2000)
jieba.add_word(u'线框图', 2000)


def len_one_filter(term):
    return (term == u'r') or (len(term) > 1)


def jieba_tokenize(text):
    # TODO: use set instead of list to filter stop words.
    tokens = jieba.cut(text, cut_all=False)
    return [t.strip() for t in tokens if len_one_filter(t) and (t.strip() not in cn_stop_words) and (not t.isspace())]


keys = loaded.keys()
# print('')
# for k in keys:
#     print(k)
docs = [u'\n'.join(loaded[k]) for k in keys]
# print(docs[5])

## tfidf
vectorizer = TfidfVectorizer(min_df=1, max_df=17, tokenizer=jieba_tokenize)
X = vectorizer.fit_transform(docs)

# print(vectorizer.get_feature_names()[:10])
# # print(vectorizer.idf_)
# # print(vectorizer.get_stop_words())
#
# lists = zip(vectorizer.get_feature_names(), vectorizer.idf_)
# sorted_idf = sorted(lists, cmp=lambda x, y: cmp(x[1], y[1]))
# to_pickle(sorted_idf, 'sorted_idf.pkl')
#
# for i in sorted_idf[:200]:
#     print(u'{0} - {1}'.format(i[0], i[1]))
#
# for i in sorted_idf[-200:]:
#     print(u'{0} - {1}'.format(i[0], i[1]))

print(len(vectorizer.get_feature_names()))
print(X.shape)


def get_important_terms(tfidf_matrix, docID):
    docRow = tfidf_matrix.toarray()[docID, :]
    vals = []
    for i, term in enumerate(docRow):
        if term > 0:
            vals.append((i, term))
    vals = sorted(vals, cmp=lambda x, y: cmp(y[1], x[1]))

    return vals


docIDs = [5, 7, 8, 10, 12, 13, 14, 15]
for docID in docIDs:
    print(u'skill: {0}'.format(keys[docID]))
    terms = get_important_terms(X, docID)
    print('{0} terms \n'.format(len(terms)))
    for i, w in terms[:100]:
        print(vectorizer.get_feature_names()[i])
    print('')

# print('')
# for k in keys:
#     print(k)
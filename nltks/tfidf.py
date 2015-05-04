# coding=utf-8
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the the the third third third one.',
    'Is this the first document?',
    'Is this the fifth document?',
    u'他来自山东省的一个小村子',
]


def jieba_tokenize(text):
    tokens = jieba.cut(text, cut_all=False)
    return list(tokens)


vectorizer = TfidfVectorizer(min_df=1, tokenizer=jieba_tokenize)
res = vectorizer.fit_transform(corpus)
# print(res.toarray())
print(res)

print(vectorizer.get_feature_names())
# print(vectorizer.idf_)
# print(vectorizer.get_stop_words())

lists = zip(vectorizer.get_feature_names(), vectorizer.idf_)
print(sorted(lists, cmp=lambda x, y: cmp(x[1], y[1])))

docID = 5
# print(res.getrow(docID))
# print(type(res.getrow(docID)))
print(res.shape)
print(len(vectorizer.get_feature_names()))


def get_important_terms(tfidf_matrix, docID):
    docRow = tfidf_matrix.toarray()[docID, :]
    vals = []
    for i, term in enumerate(docRow):
        if term > 0:
            vals.append((i, term))
    vals = sorted(vals, cmp=lambda x, y: cmp(y[1], x[1]))

    return vals

# print(vectorizer.vocabulary_.get('second'))
# print(vectorizer.vocabulary_.get('third'))
# print(vectorizer.vocabulary_.get('the'))

for i, w in get_important_terms(res, docID):
    print(vectorizer.get_feature_names()[i])

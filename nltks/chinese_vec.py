# coding=utf-8
from sklearn.feature_extraction.text import CountVectorizer
import jieba

# seg_list = jieba.cut(u'它来自山东省的一个小村子', cut_all=True)
# print '全模式：', '/ '.join(seg_list)
#
# seg_list = jieba.cut(u'This is the first document.', cut_all=True)
# print '全模式：', '/ '.join(seg_list)


def tokenize(text):
    tokens = jieba.cut(text, cut_all=False)
    return list(tokens)


vectorizer = CountVectorizer(min_df=1, tokenizer=tokenize)

analyzer = vectorizer.build_analyzer()
print(analyzer('This is a text document to analyze.'))
print(analyzer(u'它来自山东省的一个小村子'))

# ##
corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And a third one.',
    'Is this the first document?',
    u'他来自山东省的一个小村子',
]

# use jieba tokenizer
X = vectorizer.fit_transform(corpus)
print(X)

# check columns
for c in vectorizer.get_feature_names():
    print(c)

# print(vectorizer.vocabulary_.get('document'))  # 3
# print(vectorizer.vocabulary_.get(u'document'))  # 3
# print(vectorizer.vocabulary_.get('村子'))  # None
# print(vectorizer.vocabulary_.get(u'村子'))  # 17

## bi-grams
# so 'this is' is different from 'is this'
vectorizer = CountVectorizer(min_df=1, tokenizer=tokenize, ngram_range=(1, 2))
analyzer = vectorizer.build_analyzer()
print(analyzer('This is a text document to analyze.'))
print(analyzer(u'他来自山东省的一个小村子'))

##
# coding=utf-8
from snownlp import SnowNLP

# s = SnowNLP(u'这个东西真的很赞')
#
# print('words')
# for w in s.words:
#     print(w),
#
# print('tags')
# for t in s.tags:
#     print(t),
#
# print('sentiments')
# print(s.sentiments)
# print(s.pinyin)
#
#
# ## Traditional Chinese support
# s = SnowNLP(u'「繁體字」「繁體中文」的叫法在臺灣亦很常見。')
# print(s.han)


## Topic Modeling
text = u'''
当前课程图谱中所有课程之间的相似度全部基于gensim计算，
自己写的调用代码不到一百行，topic模型采用LSI(Latent semantic indexing, 中文译为浅层语义索引），
LSI和LSA（Latent semantic analysis，中文译为浅层语义分析）这两个名词常常混在一起，
事实上，在维基百科上，有建议将这两个名词合二为一。
以下是课程图谱的一个效果图，课程为著名的机器学习专家Andrew Ng教授在Coursera的机器学习公开课，
图片显示的是主题模型计算后排名前10的相关课程，Andrew Ng教授同时也是Coursera的创始人之一
'''

# s = SnowNLP(text)
# for k in s.keywords(3):
#     print(k),
#
# for sum in s.summary(5):
#     print(sum),
#     print
#

s = SnowNLP([[u'这篇', u'文章'],
             [u'那篇', u'论文'],
             [u'这个']])
print(s.tf)
print(s.idf)

print(s.sim([u'文章']))
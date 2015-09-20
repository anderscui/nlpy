# coding: utf-8
import jieba

## FUNC1: segmentation
from common.stop_words import chinese

sent = "我来到北京清华大学"

# 快，但不能解决歧义问题
seg_list = jieba.cut(sent, cut_all=True)
print "全模式：", "/ ".join(seg_list)

# 尝试精确分词，适合文本分析
seg_list = jieba.cut(sent, cut_all=False)
print "精确模式：", "/ ".join(seg_list)

# 比全模式更“全”，适合做搜索之用
sent2 = "小明硕士毕业于中国科学院计算所，后在日本京都大学深造"
seg_list2 = jieba.cut_for_search(sent2)
print "搜索引擎模式：", "/ ".join(seg_list2)

# 新词识别
sent3 = "他来到了网易杭研大厦"
seg_list3 = jieba.cut(sent3)
print "/ ".join(seg_list3)


## stop words
cn_stop_words = chinese()
cn_stop_words.append(u'一门')
cn_stop_words.append(u'任一')

jieba.add_word(u'机器学习', 2000)
jieba.add_word(u'自然语言处理', 2000)


def jieba_tokenize(text):
    tokens = jieba.cut(text, cut_all=False)
    return [t for t in tokens if t not in cn_stop_words]

sentence = u'他喜欢编程，不仅是Python，还有机器学习，自然语言处理等等，另外他还喜欢旅行和阅读。这里还有一个英文的逗号,和句号.'
print("/ ".join(jieba_tokenize(sentence)))
print("/ ".join(jieba.cut(sentence, cut_all=False)))

print(',' in cn_stop_words)
print(u',' in cn_stop_words)
print(u'.' in cn_stop_words)
print(u'强' in cn_stop_words)

## tagging

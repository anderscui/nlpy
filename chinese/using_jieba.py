# coding: utf-8
import jieba

## FUNC1: segmentation

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


## tagging

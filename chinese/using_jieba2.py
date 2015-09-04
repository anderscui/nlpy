# coding: utf-8
import jieba


def cuttest(sentence):
    seg_list = jieba.cut(sentence, cut_all=False, HMM=False)
    print "全模式：", "/ ".join(seg_list)

cuttest('我需要廉租房')
cuttest('据说这位语言学家去参加神马学术会议了')
cuttest('小明硕士毕业于中国科学院计算所，后在日本京都大学深造')
cuttest('他来到了网易杭研大厦')

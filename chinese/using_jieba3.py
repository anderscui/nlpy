# coding: utf-8
import jieba
from jieba.analyse.analyzer import ChineseTokenizer


def cuttest(sentence):
    seg_list = jieba.cut(sentence, cut_all=False, HMM=True)
    print "全模式：", "/ ".join(seg_list)

# cuttest('我需要廉租房')
# cuttest('据说这位语言学家去参加神马学术会议了')
# cuttest('小明硕士毕业于中国科学院计算所，后在日本京都大学深造')
# cuttest('他来到了网易杭研大厦')

t = ChineseTokenizer()
l = t(u'a自然语言处理bat')
# for token in l:
#     print token.text

q = [u'*{0}*'.format(token.text) for token in l]
print q
q = u' OR '.join(q)
print(q)
# cuttest('自然语言处理')
cuttest('妈妈住院了，过一段时间在说吧')
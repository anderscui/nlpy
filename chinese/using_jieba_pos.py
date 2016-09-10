# coding: utf-8
import jieba.posseg as pseg


def cuttest(text):
    words = pseg.cut(text)
    s = ' '.join('%s/%s' % (word, flag) for word, flag in words)
    print(s)

# cuttest('我需要廉租房')
# cuttest('据说这位语言学家去参加神马学术会议了')
# cuttest('小明硕士毕业于中国科学院计算所，后在日本京都大学深造')
# cuttest('他来到了网易杭研大厦')

# cuttest('我在学习自然语言处理')
# cuttest('元祐')


words = pseg.cut('整併整併')
s = ' '.join('%s/%s' % (word, flag) for word, flag in words)
print(s)

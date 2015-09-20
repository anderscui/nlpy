# coding=utf-8
import jieba
import jieba.posseg

# sent = "小明硕士毕业于中国科学院计算所，后在日本京都大学深造"
# segs = jieba.posseg.cut(sent)
#
# seg_list = list(segs)
# for s in seg_list:
#     print(s.word)
#     print(s.flag)
#     print('')


sent = "吉林的省会是长春"
segs = jieba.posseg.cut(sent)

seg_list = list(segs)
for s in seg_list:
    print(s.word)
    print(s.flag)
    print('')
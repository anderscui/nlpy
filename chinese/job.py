# coding: utf-8
import jieba

## FUNC1: segmentation

sent = "信息核对  家长表示孩子6周岁 大班 想提升孩子综合一个能力 想要让孩子测试一下一个英语的基础 看下教材方面  离SH8比较近 家长表示要安排下周六的一个时间 具体等明天课表出来后 直接预约下周6的一个测试时间"

# # 快，但不能解决歧义问题
# seg_list = jieba.cut(sent, cut_all=True)
# print "全模式：", "/ ".join(seg_list)
#
# # 尝试精确分词，适合文本分析
# seg_list = jieba.cut(sent, cut_all=False)
# print "精确模式：", "/ ".join(seg_list)

notes = ["不续费原因：高二学习紧张，因此不续费",
         "NTB6 PU3 2014.4.23与妈妈沟通学习情况，指出他是个很自信的学生，在电脑的在线测试听力是满分，也是班级里面的唯一一个，但是阅读方面还是要加强，此外在课堂上也能够自由表达自己的观点。此外提及网络课程回去还是需要按照进度完成，妈妈说好的，此外反馈他回来说有时上课纪律比较吵，听不清所讲的，希望老师严格一些。此外，邀约PTM，但妈妈说要上班，没有时间过来参加，说没有别的反馈意见，就是希望老师能够严厉一些。",
         "现在没有学英语的打算",
         "马上结束了活动妈妈说过不来了 ",
         "3.5 岁 上幼儿园 想找个英语班，孩子比较感兴趣"]

token_list = []
for note in notes:
    tokens = jieba.cut(note, cut_all=False)
    token_list += list(tokens)
    # print "/ ".join(tokens)

print(len(token_list))

token_set = set(token_list)
for token in token_set:
    print(token),
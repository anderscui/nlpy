# coding=utf-8
import glob, os, path
import jieba
from common.chinese import read_lines, write
from common.persistence import from_pickle

stopwords = set(from_pickle('stopwords.pkl'))
print len(stopwords)

for fname in glob.glob('*.txt'):
    print fname + ' started'

    name_without_ext = os.path.splitext(fname)[0]

    segmented = []

    for line in read_lines(fname):
        parts = line.strip().split('\t')

        if len(parts) < 3:
            continue

        seg_list = jieba.cut(parts[2], cut_all=False)
        seg_list = [seg for seg in seg_list if seg not in stopwords]
        s = ' '.join(seg_list)
        segmented.append(s)
        # print s

    write(name_without_ext + '.seg', '\n'.join(segmented))

    print fname + ' done'
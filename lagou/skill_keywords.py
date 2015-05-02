#encoding=utf-8
from nltk import FreqDist
from common.html_util import strip_tags
from common.persistence import from_pickle

# nlp_jobs = from_pickle('nlp.pkl')
jobs = from_pickle('ux.pkl')
print(len(jobs))

for j in jobs[:3]:
    print(j['desc'])
    print('')
    # print(strip_tags(j['desc']))
    # print('')

job_desc = [strip_tags(j['desc']) for j in jobs]

## start to parse with jieba
import jieba
# segs = jieba.cut(job_desc[0])
# print(', '.join(segs))

# print('')
# segs_all = jieba.cut(job_desc[0], cut_all=True)
# print(', '.join(segs_all))

# tokens = []
# for jd in job_desc:
#     tokens += jieba.cut(jd)
#
# print(len(tokens))
# fdist = FreqDist(tokens)
#
# cmn = fdist.most_common(200)
# for t, c in cmn:
#     print(u'{0} \t {1}'.format(t, c))
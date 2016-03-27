from common.persistence import from_pickle, to_pickle
from common.html_util import strip_tags

pos_dict = from_pickle('pos_norm.pkl')
print '%d positions' % len(pos_dict)
pid = 403932
assert pid in pos_dict
for p in pos_dict[pid]:
    print p

# get keywords of pos
print 'jieba tags'
pos = pos_dict[pid]
import jieba.analyse

tags = jieba.analyse.extract_tags(pos[2])
for t in tags:
    print t

print 'snow tags'
from snownlp import SnowNLP
s = SnowNLP(pos[2])
for t in s.keywords(limit=20):
    print t

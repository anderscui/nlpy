from nltk import ConditionalFreqDist
from nltk.corpus import inaugural

cfd = ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target))

cfd.plot()
#
# print(inaugural.fileids())
# print(inaugural.words(u'1821-Monroe.txt'))
# print(u'citizens'.lower().startswith('citizen'))
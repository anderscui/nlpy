from common.persistence import from_pickle

nlp_jobs = from_pickle('nlp.pkl')
print(len(nlp_jobs))

for j in nlp_jobs[:3]:
    print(j['desc'])
    print('')
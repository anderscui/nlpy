import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# quick example
from gensim import corpora, models, similarities

corpus = [[(0, 1.0), (1, 1.0), (2, 1.0)],
          [(2, 1.0), (3, 1.0), (4, 1.0), (5, 1.0), (6, 1.0), (8, 1.0)],
          [(1, 1.0), (3, 1.0), (4, 1.0), (7, 1.0)],
          [(0, 1.0), (4, 2.0), (7, 1.0)],
          [(3, 1.0), (5, 1.0), (6, 1.0)],
          [(9, 1.0)],
          [(9, 1.0), (10, 1.0)],
          [(9, 1.0), (10, 1.0), (11, 1.0)],
          [(8, 1.0), (10, 1.0), (11, 1.0)]]

tfidf = models.TfidfModel(corpus)
vec = [(0, 1), (4, 1)]
res = tfidf[vec]
print(res)
# scaled to unit length (Euclidean norm)
print(res[0][1]**2 + res[1][1]**2)

# transform the whole corpus via Tfidf and index it
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=12)

# query similarities
sims = index[tfidf[vec]]
print(list(enumerate(sims)))
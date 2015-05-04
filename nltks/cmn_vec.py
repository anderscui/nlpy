from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(min_df=1)
print(vectorizer)

corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
]

# default config of tokenizer
X = vectorizer.fit_transform(corpus)
# print(X)

analyzer = vectorizer.build_analyzer()
print(analyzer("This is a text document to analyze."))
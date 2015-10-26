from collections import Counter

# simple usage
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print cnt

# merge counters
cnt1 = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
cnt2 = cnt + cnt1
print cnt2

# nested/loops
docs = [['red', 'blue', 'red', 'green', 'blue', 'blue'],
        ['red', 'green', 'red', 'green', 'blue', 'blue'],
        ['red', 'green', 'green', 'green', 'blue', 'blue'],
        ['green', 'green', 'green', 'blue', 'blue'],
        ['red', 'red', 'green']
        ]

cnt_word_doc = Counter()
cnt_words = Counter()
for doc in docs:
    cur = Counter(doc)
    for k in cur:
        cnt_word_doc[k] += 1
        cnt_words[k] += cur[k]

print cnt_word_doc
print cnt_words

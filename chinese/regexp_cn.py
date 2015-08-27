# coding=utf-8
import re

# Chinese
s = u'全部共494条'
m = re.search(r'\d+', s)
print(m.group())

# group text
movie_url = 'http://movie.douban.com/subject/123/comments?start=0&limit=20&sort=time'
pat = 'ex'
m = re.search('start=(\d+)', movie_url)
print(m.group(1))


re_han = re.compile("([\u4E00-\u9FA5]+)")
re_skip = re.compile("(\d+\.\d+|[a-zA-Z0-9]+)")

print re.split('(\W+)', 'Words, words, words.')
print re.split('(\w+)', 'Words, words, words.')


s = u'Python 2.7, Java 8'
tmp = re_skip.split(s)
for x in tmp:
    if x:
        print x

# coding=utf-8
import re

s = 'Hello, Python & Regex'
m = re.search('th', s)
print(m.group())

# Chinese
s = u'全部共494条'
m = re.search(r'\d+', s)
print(m.group())

# group text
movie_url = 'http://movie.douban.com/subject/123/comments?start=0&limit=20&sort=time'
pat = 'ex'
m = re.search('start=(\d+)', movie_url)
print(m.group(1))
# coding=utf-8
import re

s = 'Hello, Python & Regex'
m = re.search('th', s)
print(m.group())

# Chinese
s = u'全部共494条'
m = re.search(r'\d+', s)
print(m.group())


s = u'10k以上'
m = re.search(u'(\d+)k以上', s)
if m:
    print m.groups()
    print m.group(0), m.group(1)
else:
    m = re.search(u'(\d+)k以下', s)
    print m.groups()
    print m.group(0), m.group(1)


# group text
movie_url = 'http://movie.douban.com/subject/123/comments?start=0&limit=20&sort=time'
pat = 'ex'
m = re.search('start=(\d+)', movie_url)
print(m.group(1))


print re.split('\W+', 'Words, words, words.')
print re.split('\w+', 'Words, words, words.')


## lagou salary parsing
def parse_salary(s):
    m = re.search(u'(\d+)k以上', s)
    if m:
        return int(m.group(1))*1000, 10**6

    m = re.search(u'(\d+)k以下', s)
    if m:
        return 0, int(m.group(1))*1000

    m = re.search(u'(\d+)k-(\d+)k', s)
    if m:
        return int(m.group(1))*1000, int(m.group(2))*1000
    return 0, 0


print(parse_salary(u'10k以上'))
print(parse_salary(u'10k以下'))
print(parse_salary(u'10k-20k'))
print(parse_salary(u'ak-20k'))
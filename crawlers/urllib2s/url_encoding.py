# coding=utf-8
from urllib import urlencode, quote, quote_plus

url = u'C#'
print(quote(url))

url = '研究/开发'
print(quote(url))

url = '研究/开发'
print(quote_plus(url))

w = u'C#'
print(w.replace('#', '%23'))

w = u'研究/开发'
print(w.replace('/', '%2B'))
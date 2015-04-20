__author__ = 'andersc'

import urllib2
resp = urllib2.urlopen('http://www.douban.com')
html = resp.read()
print(html)
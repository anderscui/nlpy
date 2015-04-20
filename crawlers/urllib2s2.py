__author__ = 'andersc'

import urllib2
req = urllib2.Request('http://www.douban.com')
resp = urllib2.urlopen(req)
html = resp.read()
print(html)
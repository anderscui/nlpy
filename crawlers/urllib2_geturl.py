import urllib2

start = 'http://dou.bz/1sjiGw'
req = urllib2.Request(start)
resp = urllib2.urlopen(req)
print('start with: ' + start)
print('end with: ' + resp.geturl())
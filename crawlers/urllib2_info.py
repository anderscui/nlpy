from urllib2 import Request, urlopen, URLError, HTTPError

old_url = 'http://dou.bz/1sjiGw'
req = Request(old_url)
resp = urlopen(req)
print('Info(): ')
print(resp.info())
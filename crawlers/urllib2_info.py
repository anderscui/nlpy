<<<<<<< Updated upstream
from urllib2 import Request, urlopen, URLError, HTTPError

old_url = 'http://dou.bz/1sjiGw'
req = Request(old_url)
resp = urlopen(req)
print('Info(): ')
print(resp.info())
=======
import urllib2

start = 'http://dou.bz/1sjiGw'
req = urllib2.Request(start)
resp = urllib2.urlopen(req)
print('resp info: ')
print resp.info()
>>>>>>> Stashed changes

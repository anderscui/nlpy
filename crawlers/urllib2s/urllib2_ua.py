import urllib
import urllib2

url = 'http://www.douban.com/update'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
values = {'name': '',
          'pwd': ''}
headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
resp = urllib2.urlopen(req)
html = resp.read()
print(html)
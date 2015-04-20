import urllib
import urllib2

url = 'http://www.douban.com/accounts/login'
values = {'form_email': '',
          'form_password': ''}
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
resp = urllib2.urlopen(req)
html = resp.read()
print(html)
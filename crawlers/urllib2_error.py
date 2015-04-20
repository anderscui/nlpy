import urllib
import urllib2

url = 'http://bbs.csdn.net/callherplease'
req = urllib2.Request(url)

## method 1
# try:
#     resp = urllib2.urlopen(req)
#     html = resp.read()
#     print(html)
# except urllib2.HTTPError, e:
#     print('http error occured')
#     print(e.code)
# except urllib2.URLError, e:
#     print('server not reachable')
#     print(e.code)
# else:
#     print('you are very lucky:)')


## method 2
try:
    resp = urllib2.urlopen(req)
    html = resp.read()
    print(html)
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print('http error occured')
        print(e.code)
    elif hasattr(e, 'reason'):
        print('server not reachable')
        print(e.reason)
else:
    print('you are very lucky:)')


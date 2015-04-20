import string, urllib2

def baidu_tieba(url, page_start, page_end):
    for i in range(page_start, page_end+1):
        fname = string.zfill(i, 5) + '.html'
        print('downloading ' + str(i) + ' page which is stored as ' + fname + '......')
        f = open(fname, 'w+')

        req = urllib2.Request(url + str(i))
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Gecko/20100101 Firefox/36.0')
        req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        req.add_header('Referer', 'http://pos.baidu.com/wh/o.htm?ltr=')
        req.add_header('Cookie', 'BAIDUID=417CE0EC0BF748806F1812F748F1CFE5:FG=1; BDUSS=JIdW8zOGl-ZDhuOHd6dlZxOTBBQU5YQllZTUowRGdHMjhPYUhzQlhZbWZiUUJWQVFBQUFBJCQAAAAAAAAAAAEAAAARKelBZW5qb3m038PfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ~g2FSf4NhURF; Hm_lvt_f1b3494dce64562f2391e4fb95c5358d=1425828158; BAIDUPSID=417CE0EC0BF748806F1812F748F1CFE5')
        m = urllib2.urlopen(req).read()
        f.write(m)
        f.close()

url = 'http://tieba.baidu.com/p/2329550549'

baidu_tieba(url, 1, 5)

# coding=utf-8

from bs4 import BeautifulSoup
from urllib2 import urlopen
from common.chinese import read_all, write


BASE_URL = 'http://www.lagou.com/'

job_list_url = u'http://www.lagou.com/jobs/list_{0}?kd={1}&spc=1&pl=&gj=&xl=&yx=&gx=&st=&labelWords=&lc=&workAddress=&city={2}&requestId=&pn={3}'

job_detail_url_format = 'http://www.lagou.com/jobs/143205.html?source=search'

def make_url(keyword, city, pn):
    return job_list_url.format(keyword, keyword, city, pn)


def make_soup(url):
    html = urlopen(url.encode('utf-8')).read()
    return BeautifulSoup(html, "lxml")


def make_html_filename(keyword, city, pn):
    return u'{0}-{1}-{2}.html'.format(keyword, city, pn)


def save_html(url, file_name):
    html = urlopen(url.encode('utf-8')).read()
    # print(html)
    write('./html/' + file_name, html.decode('utf-8'))


def make_soup_from_file(file_name):
    html = read_all('./html/' + file_name)
    return BeautifulSoup(html, 'lxml')


def get_category_links(section_url):
    soup = make_soup(section_url)
    boccat = soup.find('dl', 'boccat')
    category_links = [BASE_URL + dd.a['href'] for dd in boccat.findAll('dd')]

    return category_links


def get_category_winner(category_url):
    soup = make_soup(category_url)
    category = soup.find('h1', 'headline').string

    print(category)
    if not category:
        winner = None
        runners_up = None
    else:
        winner = [h2.string for h2 in soup.findAll('h2', 'boc1')]
        runners_up = [h2.string for h2 in soup.findAll('h2', 'boc2')]

    return {"category": category,
            "category_url": category_url,
            "winner": winner,
            "runners_up": runners_up}


if __name__ == '__main__':
    keyword = u'数据挖掘'
    city = u'全国'
    pn = 1
    url = make_url(keyword, city, 1)
    print(url)
    # soup = make_soup(job_list_url)
    # print(soup.title)

    html_file_name = make_html_filename(keyword, city, pn)
    print(html_file_name)
    save_html(url, html_file_name)

    soup = make_soup_from_file(html_file_name)
    print(soup.title.string)
    pos_list = soup.find('ul', 'hot_pos reset')
    # print(pos_list)
    p_pos = pos_list.find_all('li', recursive=False)

    for pos in p_pos:
        print(pos.string)
        spans = pos.find_all("span")
        for s in spans:
            print(s.text)

# coding=utf-8

from bs4 import BeautifulSoup
from urllib2 import urlopen
from common.chinese import read_all, write


BASE_URL = 'http://www.lagou.com/jobs/'

job_list_url = u'http://www.lagou.com/jobs/list_{0}?kd={0}&spc=1&pl=&gj=&xl=&yx=&gx=&st=&labelWords=&lc=&workAddress=&city={1}&requestId=&pn={2}'


def make_url(keyword, city, pn):
    return job_list_url.format(keyword, city, pn)


def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")


def save_html(url):
    html = urlopen(url).read()
    write('./lagou.txt', html.decode('utf-8'))


def make_soup_from_file():
    html = read_all('./lagou.txt')
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
    city = u'上海'
    pn = 1
    url = make_url(keyword, city, 1)
    print(url)
    # soup = make_soup(job_list_url)
    # print(soup.title)

    soup = make_soup_from_file()
    print(soup.title.string)
    pos_list = soup.find('ul', 'hot_pos')
    print(len(pos_list))
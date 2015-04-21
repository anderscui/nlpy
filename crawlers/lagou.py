# coding=utf-8
import re

from bs4 import BeautifulSoup
from urllib2 import urlopen, URLError
import time
from common.chinese import write, read_all
from common.persistence import to_pickle, from_pickle

BASE_URL = 'http://www.lagou.com/'

skill_url = BASE_URL + 'jobs/list_{0}?kd={0}&spc=1&pl=&gj=&xl=&yx=&gx=&st=&labelWords=label&lc=&workAddress=&city' \
                       '={1}&requestId=&pn={2}'
skill_url = unicode(skill_url)

job_detail_url = 'http://www.lagou.com/jobs/{0}.html?source=search'


def make_search_url(urlfmt, keyword, city, pn):
    return urlfmt.format(keyword, city, pn)


def make_html(url):
    return urlopen(url).read()


def make_soup(html):
    return BeautifulSoup(html, "lxml")


def save_jobs_html(url, skill, pn=1):

    try:
        html = urlopen(url.encode('utf-8')).read()
    except URLError, e:
        if hasattr(e, 'code'):
            print(u'http error occured for skill: {0}, code: {1}'.format(skill, e.code))
        elif hasattr(e, 'reason'):
            print('server not reachable: ' + e.reason)

        return ''
    else:
        write(u'./html/{0}_{1}.html'.format(skill, pn), html.decode('utf-8'))
        return html


def download_search_results(skill_url_fmt, kd, city, page):
    url = make_search_url(skill_url_fmt, kd, city, page)
    html = save_jobs_html(url, kd, page)
    time.sleep(1)

    if not html:
        return None

    currPage = re.search(r'currPage: (\d+)', html)
    pageCount = re.search(r'pageCount: (\d+)', html)

    if currPage and pageCount:
        curr = int(currPage.group(1))
        pageCount = int(pageCount.group(1))

        if curr < pageCount:
            download_search_results(skill_url_fmt, kd, city, curr + 1)


def save_html(url, file_name):
    print(url)
    print(file_name)
    html = urlopen(url).read()
    print(html)
    write('./html/' + file_name, html.decode('utf-8'))


def category_contents(cat_tag):
    header = cat_tag.find('div', 'menu_main').find('h2').text
    # print(u'** {0} **'.format(header))

    sub_cats_tags = cat_tag.find_all('dl')
    sub_cats = []

    for sub in sub_cats_tags:
        sub_cat_name = sub.find('dt').find('a').text.strip()
        sub_cat_list = [(kw.text, kw['href']) for kw in sub.find('dd').find_all('a')]

        sub_cats.append((sub_cat_name, sub_cat_list))

    return {'name': header,
            'sub_cats': sub_cats}


if __name__ == '__main__':
    # # home page - skills
    start_url = BASE_URL
    start_page = 'lagou_home.html'
    # save_html(start_url, start_page)

    # html = read_all('./html/' + start_page)
    # soup = make_soup(html)
    #
    # main_navs = soup.find('div', 'mainNavs')
    # cat_tags = main_navs.find_all('div', 'menu_box')
    # cats = {}
    # for i, cat in enumerate(cat_tags):
    # cats[i] = category_contents(cat)
    #
    # for i in cats:
    # cat = cats[i]
    #     print(u'** {0} **'.format(cat['name']))
    #     for sub in cat['sub_cats']:
    #         print(sub[0])
    #         for skill, href in sub[1]:
    #             print('\t-' + skill + ' - ' + href)
    #
    # to_pickle(cats, 'cats.pkl')


    # ## jobs of one skill

    # # skill_url = 'http://www.lagou.com/zhaopin/ziranyuyanchuli?labelWords=label'
    # spelling = 'ziranyuyanchuli'
    page = 1
    city = u'全国'
    # kd = u'自然语言处理'
    # search_url = make_search_url(skill_url, kd, city, page)

    # download_search_results(skill_url, kd, city, page)

    cs = 'C%23'
    skip_list = ['Java', 'Python', 'PHP', '.NET']
    cats = from_pickle('cats.pkl')
    for i in cats:
        cat = cats[i]
        print(u'** cat {0}: {1} **'.format(i, cat['name']))
        for sub in cat['sub_cats']:
            print(sub[0])

            for skill, href in sub[1]:
                if skill in skip_list:
                    print('skip ' + skill)
                    continue

                print('\t-' + skill + ' - ' + href)
                if skill == 'C#':
                    skill = cs

                # print(make_search_url(skill_url, skill, city, page))
                download_search_results(skill_url, skill, city, page)

    # print(search_url)
    # save_jobs_html(search_url, spelling, page)

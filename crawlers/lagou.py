from bs4 import BeautifulSoup
from urllib2 import urlopen
from common.chinese import write, read_all

BASE_URL = 'http://www.lagou.com/'


def make_html(url):
    return urlopen(url).read()


def make_soup(html):
    return BeautifulSoup(html, "lxml")


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


def save_html(url, file_name):
    print(url)
    print(file_name)
    html = urlopen(url).read()
    print(html)
    write('./html/' + file_name, html.decode('utf-8'))


def save_jobs_html(url, skill, pn=1):
    html = urlopen(url).read()
    print(html)
    write('./html/' + '{0}_{1}.html'.format(skill, pn), html.decode('utf-8'))


def category_contents(cat_tag):
    # header = cat_tag.find('div', 'menu_main').find('h2')
    header = cat_tag.find('div', 'menu_main').find('h2').text

    sub_cats = cat_tag.find_all('dl')
    for sub in sub_cats:
        print(sub.find('dt').find('a').text.strip())
        for kw in sub.find('dd').find_all('a'):
            print('\t-' + kw.text + ' - ' + kw['href'])

    return {'header': header}


if __name__ == '__main__':
    # # home page - skills
    # start_url = BASE_URL
    # start_page = 'lagou_home.html'
    # # save_html(start_url, start_page)
    #
    # html = read_all('./html/' + start_page)
    # soup = make_soup(html)
    #
    # main_navs = soup.find('div', 'mainNavs')
    # categories = main_navs.find('div', 'menu_box')
    # category_contents(categories)

    ## jobs of one skill
    skill_url = 'http://www.lagou.com/zhaopin/ziranyuyanchuli?labelWords=label'
    spelling = 'ziranyuyanchuli'
    page = 1
    save_jobs_html(skill_url, spelling, page)

    # winners = [get_category_winner(clink) for clink in get_category_links(url)[:2]]
    #
    # for w in winners:
    #     print(w['winner'])
    #     # print(', '.join(w['winner']))
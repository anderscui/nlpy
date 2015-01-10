from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = 'http://www.chicagoreader.com'


def make_soup(url):
    html = urlopen(url).read()
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


if __name__ == '__main__':
    url = 'http://www.chicagoreader.com/chicago/best-of-chicago-2011-food-drink/BestOf?oid=4106228'
    winners = [get_category_winner(clink) for clink in get_category_links(url)[:2]]

    for w in winners:
        print(w['winner'])
        # print(', '.join(w['winner']))
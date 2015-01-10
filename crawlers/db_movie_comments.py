# coding=utf-8

import codecs
import re

from bs4 import BeautifulSoup
from urllib2 import urlopen
import time


rating_dict = {u'力荐': 5,
               u'推荐': 4,
               u'还行': 3,
               u'较差': 2,
               u'很差': 1}


def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")


def get_ratings(mid, url):
    soup = make_soup(url)
    base_url = 'http://movie.douban.com/subject/{0}/comments'.format(mid)

    title_line = soup.find('div', 'title_line')
    sub_title = u'短评'

    total_info = title_line.find('span', 'fleft').string
    m_total = re.search(r'\d+', total_info)
    total = 0
    if m_total:
        total = int(m_total.group())

    paginator = soup.find(id='paginator')
    next_a = paginator.find('a', 'next')

    print('mid: ' + str(mid))
    print('title: ' + soup.title.string.rstrip(sub_title).strip())
    print('total: ' + str(total))
    print('next url: ' + next_a['href'])

    comments = soup.find(id='comments')
    comment_items = comments.findAll('div', {'class': 'comment'})

    ratings_page = {'mid': mid,
                    'title': soup.title.string,
                    'total': total,
                    'next_url': base_url + next_a['href']}
    rates = []
    for ci in comment_items:
        rating = ci.find('span', 'rating')
        rating_text = u'未打分'
        if rating:
            rating_text = rating['title']

        p = ci.p
        rating_p = ''
        if p and p.string:
            rating_p = p.string

        rates.append({'rating': rating_text,
                      'review': rating_p})

    ratings_page['ratings'] = rates

    return ratings_page


def save_ratings(movie_ids, at_most=None):

    for mid in movie_ids:
        start_url = movie_url.format(mid)
        file_name = 'moviews_{0}.txt'.format(mid)

        prev_start = -1
        next_url = start_url
        has_read = 0
        total = 1
        first_page = True

        with codecs.open(file_name, 'w', 'utf-8') as f:

            while has_read < total and next_url:

                m = re.search('start=(\d+)', next_url)
                if not m:
                    break
                else:
                    cur_start = int(m.group(1))
                    if cur_start < prev_start:
                        break

                if at_most and has_read > at_most:
                    break

                ratings = get_ratings(mid, next_url)
                total = ratings['total']
                next_url = ratings['next_url']

                if first_page:
                    f.write('movie id - ' + str(ratings['mid']) + '\n')
                    f.write(ratings['title'] + '\n')
                    f.write(str(ratings['total']) + '\n')
                    f.write('********************\n\n')
                    first_page = False

                if not len(ratings['ratings']):
                    break

                for s in ratings['ratings']:
                    f.write(s['rating'] + '\n')
                    f.write(s['review'].strip() + '\n')
                    f.write('**********\n\n')
                    has_read += 1

                prev_start = cur_start

                # don't send the requests too frequently
                time.sleep(2)

        print('done for movie: ' + str(mid))
        print(f.closed)


if __name__ == '__main__':
    # PAGE_LIMIT = 20
    # BASE_URL = 'http://movie.douban.com/subject/25964630/comments'

    movie_url = 'http://movie.douban.com/subject/{0}/comments?start=0&limit=20&sort=time'

    # # 另一个故乡
    # mid = 22265121
    # # 布达佩斯大饭店
    # mid = 11525673
    # # 哆啦A梦
    # mid = 25769362
    # # 互联网之子
    # mid = 25785114
    # # 宇宙快递
    # mid = 25884822
    # # 权力的游戏 第四季
    # mid = 23232876
    # # 战长沙
    # mid = 20258941
    # # 匆匆那年
    # mid = 25840705
    # # 昼颜
    # mid = 25897313
    # # 爸爸去哪儿 第二季
    # mid = 25826679
    # # Her
    # mid = 6722879

    # movie_ids = [25769362, 25785114, 25884822, 23232876, 20258941, 25840705, 25897313, 25826679, 6722879]
    # save_ratings(movie_ids, at_most=5)

    # done: 21352814, 24843198, 6973376
    movie_ids = [24404677, 7054604, 6537500, 25805741, 23034934, 10808442,
                 10535568, 6786002, 1418834, 20436812, 11525673]
    save_ratings(movie_ids)
# coding=utf-8
from _socket import timeout
import glob
import httplib
import os
import re
import socket

from bs4 import BeautifulSoup
from urllib2 import urlopen, URLError, Request
import time
import datetime
import sys

from common.chinese import write, read_all
from common.io import created_on
from common.persistence import to_pickle, from_pickle
from models import Job, Company, unified

debug = False

BASE_URL = 'http://www.lagou.com/'

skill_url = BASE_URL + 'jobs/list_{0}?kd={0}&spc=1&pl=&gj=&xl=&yx=&gx=&st=&labelWords=label&lc=&workAddress=&city' \
                       '={1}&requestId=&pn={2}'
skill_url = unicode(skill_url)

job_detail_url = 'http://www.lagou.com/jobs/{0}.html?source=search'

# set sockets
socket_timeout = 20
sleep_seconds = 5

socket.setdefaulttimeout(socket_timeout)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0'}


def log(o):
    if debug:
        print(o)


def make_search_url(urlfmt, keyword, city, pn):
    return urlfmt.format(keyword, city, pn)


def make_html(url):
    req = urlopen(url)
    res = req.read()
    req.close()
    return res


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

    html_file = u'./html/{0}_{1}.html'.format(kd, page)
    if os.path.exists(html_file):
        print(html_file + u' already exists')
        return

    url = make_search_url(skill_url_fmt, kd, city, page)
    html = save_jobs_html(url, kd, page)
    time.sleep(2)

    if not html:
        return None

    currPage = re.search(r'currPage: (\d+)', html)
    pageCount = re.search(r'pageCount: (\d+)', html)

    if currPage and pageCount:
        curr = int(currPage.group(1))
        pageCount = int(pageCount.group(1))

        if curr < pageCount:
            download_search_results(skill_url_fmt, kd, city, curr + 1)


def download_all_search_results():
    page = 1
    city = u'全国'
    # skip_list = ['Java', 'Python']
    skip_list = []
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
                if '#' in skill or '/' in skill:
                    skill = quoted(skill)

                download_search_results(skill_url, skill, city, page)


def save_job_detail_html(skill, job_id):
    global sleep_seconds

    if sleep_seconds >= 30:
        print(u'it already took you a long time to wait, take a rest now:) ')
        sys.exit(10)

    html_file = u'./detail/{0}_{1}.html'.format(skill, job_id)
    if os.path.exists(html_file):
        print(html_file + u' already exists')
        return

    url = job_detail_url.format(job_id)
    try:
        url_req = Request(url.encode('utf-8'), headers=headers)
        req = urlopen(url_req)
        html = req.read()
        req.close()
    except UnicodeDecodeError, e:
        print(str(job_id) + ' unicode error: ' + e.message)
        return ''
    except URLError, e:
        print(str(job_id) + ' download error: ' + e.message)
        return ''
    except timeout:
        sleep_seconds += 5
        print(u'timeout ({0}-{1}) error occurred, take a rest now. zzZZZ...'.format(skill, job_id))
        time.sleep(60)
    except httplib.BadStatusLine, e:
        print(str(job_id) + ' bad status error: ' + e.message)
    else:
        write(html_file, html.decode('utf-8'))
        return html


def get_job_list_from_html(html_file):
    return None


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


def save_keywords(html_file):
    html = read_all(html_file)
    soup = make_soup(html)

    main_navs = soup.find('div', 'mainNavs')
    cat_tags = main_navs.find_all('div', 'menu_box')
    cats = {}
    for i, cat in enumerate(cat_tags):
        cats[i] = category_contents(cat)

    for i in cats:
        cat = cats[i]
        print(u'** {0} **'.format(cat['name']))
        for sub in cat['sub_cats']:
            print(sub[0])
            for skill, href in sub[1]:
                print('\t-' + skill + ' - ' + href)

    to_pickle(cats, 'cats.pkl')


def get_published_date(dt, created_time):
    if ':' in dt:
        parts = dt.split(':')
        assert len(parts) == 2
        return created_time.replace(hour=int(parts[0]), minute=int(parts[1]), second=0, microsecond=0)
    elif '-' in dt:
        return datetime.datetime.strptime(dt, '%Y-%m-%d')
    else:
        # should be like u'2天前'
        days = int(re.search('\d+', dt).group(0))
        return created_time.date() + datetime.timedelta(days=-days)


def read_job_from_html(skill, html_file):
    """
    read job info from downloaded html file
    :param html_file: contains job info, but sometime the contents are empty.
    """
    html = read_all(html_file)
    soup = make_soup(html)
    detail = soup.find('dl', 'job_detail')

    # in some rare cases, e.g. the job is closed already, then the job info is missing.
    if not detail:
        return None

    job = Job()

    job.job_id = int(soup.find('input', {'id': 'jobid'})['value'])
    job.skill_tag = skill

    log('*** JOB ***')
    title = detail.find('h1')
    log(title['title'])
    log(title.div.text)

    job.title = title['title']
    job.dept = title.div.text

    log('')
    request = detail.find('dd', 'job_request')
    main_features = []
    for s in request.stripped_strings:
        f = s.strip().lstrip(u'职位诱惑 : ').lstrip(u'发布时间：').rstrip(u'发布')
        log(f)
        main_features.append(f)

    assert len(main_features) == 7
    job.salary = main_features[0]
    job.city = main_features[1]
    job.experience = main_features[2]
    job.education = main_features[3]
    job.full_time = main_features[4] == u'全职'
    job.benefits = main_features[5]
    job.published_date = get_published_date(main_features[6], created_on(html_file))

    log('')
    desc_html = []
    desc = detail.find('dd', 'job_bt').find_all('p')
    for bt in desc:
        desc_html.append(unicode(bt))
    job.desc = ''.join(desc_html)
    log(job.desc)

    log('\n*** COMPANY ***\n')
    company = Company()

    comp = soup.find('dl', 'job_company')
    url = comp.dt.a['href']
    pat = re.compile(r'(?P<comp_id>\d+)')
    m = re.search(pat, url)
    log(url)
    company.comp_id = int(m.group('comp_id'))
    job.comp_id = company.comp_id

    log(comp.dt.a.img['src'])
    log(comp.dt.a.div.h2.text.split()[0])
    company.logo = comp.dt.a.img['src']
    company.name = comp.dt.a.div.h2.text.split()[0]

    log('')
    comp_features = comp.dd
    features = []
    for li in comp_features.ul.find_all('li'):
        for ls in li.stripped_strings:
            features.append(ls)

    log(''.join(features))
    if len(features) == 6:
        company.domain = features[1]
        company.size = features[3]
        company.url = features[5]
    else:
        print(u'features ex: ' + html_file)

    log('')
    stage_h = comp_features.h4
    stage_tags = stage_h.find_next_sibling('ul').find_all('li')
    stage = []
    for li in stage_tags:
        for ls in li.stripped_strings:
            stage.append(ls)
    log('\t'.join(stage))
    if len(stage) % 2 == 0:
        for i in xrange(0, len(stage), 2):
            if stage[i] == u'目前阶段':
                company.cur_stage = stage[i + 1]
            elif stage[i] == u'投资机构':
                company.investor = stage[i + 1]
    else:
        print(u'stages ex: ' + html_file)

    log('')
    # address
    if comp_features.div:
        log(comp_features.div.text)
        company.address = comp_features.div.text

    return job, company


def show_obj(obj):
    properties = [p for p in dir(obj) if not p.startswith('_')]
    for p in properties:
        print(u'prop: {0}, val: {1}'.format(p, obj.__getattribute__(p)))


def download_job_details(skill):
    existing = glob.glob1('detail', skill + u'_*.html')
    if existing:
        print(u'{0} has been downloaded'.format(skill))
        return

    for f in glob.glob(skill + u'*.html'):
        hp = os.path.join(os.getcwdu(), f)
        print(f)

        html = read_all(hp)
        soup = make_soup(html)
        for li in soup.find('ul', 'hot_pos reset').find_all('li', recursive=False):
            save_job_detail_html(skill, li['data-jobid'])
            print(li['data-jobid'] + ' downloaded.')
            time.sleep(sleep_seconds)


def download_all_job_details():

    print('>>start to download job details of all tags...')

    cats = from_pickle('cats.pkl')

    os.chdir('./html')
    print(os.getcwdu())

    for i in cats:
        cat = cats[i]
        print(u'** cat {0}: {1} **'.format(i, cat['name']))
        for sub in cat['sub_cats']:
            for skill, href in sub[1]:
                print('downloading... ' + skill)
                if '#' in skill or '/' in skill:
                    skill = quoted(skill)

                download_job_details(skill)

    os.chdir('../../lagou')
    print(os.getcwdu())

    print('<<end to download job details of all tags...')


def quoted(s):
    return s.replace('#', '%23').replace('/', '%2B')


def load_job_data():

    start = datetime.datetime.now()

    cats = from_pickle('cats.pkl')

    os.chdir('./html/detail')
    print(os.getcwd())

    detail_html_paths = []
    for i in cats:
        cat = cats[i]
        print(u'** cat {0}: {1} **'.format(i, cat['name']))
        for sub in cat['sub_cats']:
            for skill, href in sub[1]:
                print('loading... ' + skill)
                if '#' in skill or '/' in skill:
                    skill = quoted(skill)

                for f in glob.glob(skill + u'_*.html'):
                    hp = os.path.join(os.getcwdu(), f)
                    # print(hp)
                    detail_html_paths.append((skill, hp))

    os.chdir('../..')
    print(os.getcwd())

    all_jobs = []
    all_comps = {}
    all_jc = {}
    counter = 0
    for skill, detail_file in detail_html_paths:
        job = read_job_from_html(skill, detail_file)
        if job:
            j, c = job

            all_jobs.append(j)
            if c.comp_id not in all_comps:
                all_comps[c.comp_id] = c

            counter += 1
            if counter % 50 == 0:
                print(counter)
            uni = unified(j, c)
            all_jc[j.job_id] = uni

    print(counter)
    print(len(all_jobs))
    print(len(all_comps))
    print(len(all_jc))

    to_pickle(all_jobs, 'jobs.pkl')
    to_pickle(all_comps, 'comps.pkl')
    to_pickle(all_jc, 'unified.pkl')

    print(start)
    print(datetime.datetime.now())


if __name__ == '__main__':

    os.chdir('../crawlers')

    # # home page - skills
    start_url = BASE_URL
    start_page = 'lagou_home.html'
    # save_html(start_url, start_page)

    ################################

    # save_keywords('./html/' + start_page)

    ################################

    # download_all_search_results()

    ################################

    download_all_job_details()

    ################################

    ### load job data from html files, time: 10 minutes for 9900 jobs.
    # load_job_data()
    ### load job data from html files end.

    # u'黑盒测试'
    # u'运维工程师'
    # u'病毒分析'
    # u'技术总监'
    # u'运维总监'
    # u'项目总监'
    # u'安全专家'
    # u'项目经理'
    # u'项目助理'
    # u'硬件'
    # u'驱动开发'
    # u'模具设计'
    # u'材料工程师'
    # u'电商产品经理'
    # u'产品实习生'
    # u'Flash设计师'
    # u'多媒体设计师'
    # u'视觉设计师'
    # u'游戏场景'
    # u'游戏数值策划'
    # u'无线交互设计师'

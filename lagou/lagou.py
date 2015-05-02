# coding=utf-8
import glob
import os
import re

from bs4 import BeautifulSoup
from urllib2 import urlopen, URLError
import time
import datetime

from common.chinese import write, read_all
from common.io import created_on
from common.persistence import to_pickle, from_pickle
from models import Job, Company, unified

BASE_URL = 'http://www.lagou.com/'

skill_url = BASE_URL + 'jobs/list_{0}?kd={0}&spc=1&pl=&gj=&xl=&yx=&gx=&st=&labelWords=label&lc=&workAddress=&city' \
                       '={1}&requestId=&pn={2}'
skill_url = unicode(skill_url)

job_detail_url = 'http://www.lagou.com/jobs/{0}.html?source=search'

debug = False


def log(o):
    if debug:
        print(o)


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


def save_job_detail_html(skill, job_id):
    url = job_detail_url.format(job_id)
    try:
        html = urlopen(url.encode('utf-8')).read()
    except URLError, e:
        if hasattr(e, 'code'):
            print(u'http error occured for job: {0}, code: {1}'.format(job_id, e.code))
        elif hasattr(e, 'reason'):
            print('server not reachable: ' + e.reason)

        return ''
    else:
        write(u'./detail/{0}_{1}.html'.format(skill, job_id), html.decode('utf-8'))
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
    assert len(features) == 6
    company.domain = features[1]
    company.size = features[3]
    company.url = features[5]

    log('')
    stage_h = comp_features.h4
    stage_tags = stage_h.find_next_sibling('ul').find_all('li')
    stage = []
    for li in stage_tags:
        for ls in li.stripped_strings:
            stage.append(ls)
    log('\t'.join(stage))
    for i in xrange(0, len(stage), 2):
        if stage[i] == u'目前阶段':
            company.cur_stage = stage[i + 1]
        elif stage[i] == u'投资机构':
            company.investor = stage[i + 1]

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
    for f in glob.glob(skill + u'*.html'):
        hp = os.path.join(os.getcwdu(), f)
        print(f)

        html = read_all(hp)
        soup = make_soup(html)
        for li in soup.find('ul', 'hot_pos reset').find_all('li', recursive=False):
            save_job_detail_html(skill, li['data-jobid'])
            print(li['data-jobid'] + ' downloaded.')
            time.sleep(1)


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
    # print(u'** {0} **'.format(cat['name']))
    # for sub in cat['sub_cats']:
    #         print(sub[0])
    #         for skill, href in sub[1]:
    #             print('\t-' + skill + ' - ' + href)
    #
    # to_pickle(cats, 'cats.pkl')


    # ## jobs of one skill
    # # skill_url = 'http://www.lagou.com/zhaopin/ziranyuyanchuli?labelWords=label'
    # spelling = 'ziranyuyanchuli'
    # page = 1
    # city = u'全国'
    # # kd = u'自然语言处理'
    # # search_url = make_search_url(skill_url, kd, city, page)
    #
    # # download_search_results(skill_url, kd, city, page)
    #
    # # process #, /
    # cs = 'C%23'
    # # skip_list = ['Java', 'Python', 'PHP', '.NET']
    # skip_list = []
    # cats = from_pickle('cats.pkl')
    # for i in cats:
    #     cat = cats[i]
    #     print(u'** cat {0}: {1} **'.format(i, cat['name']))
    #     for sub in cat['sub_cats']:
    #         print(sub[0])
    #
    #         for skill, href in sub[1]:
    #             if skill in skip_list:
    #                 print('skip ' + skill)
    #                 continue
    #
    #             print('\t-' + skill + ' - ' + href)
    #             if skill == 'C#':
    #                 skill = cs
    #
    #             # print(make_search_url(skill_url, skill, city, page))
    #             download_search_results(skill_url, skill, city, page)

    # print(search_url)
    # save_jobs_html(search_url, spelling, page)
    # jid = 128328
    # print(save_job_detail_html(jid))

    # start_skills = [u'Python', u'自然语言处理', u'数据挖掘', u'搜索算法', u'精准推荐', u'用户研究员', u'交互设计师', u'.NET']
    # start_skills = [u'自然语言处理']
    # cats = from_pickle('cats.pkl')
    # for i in cats:
    #     cat = cats[i]
    #     print(u'** cat {0}: {1} **'.format(i, cat['name']))
    #     for sub in cat['sub_cats']:
    #         # print(sub[0])
    #
    #         for skill, href in sub[1]:
    #             if skill in start_skills:
    #                 print('downloading... ' + skill)
    #                 continue

    ### download jobs of specific skills
    start_skills = [u'Python', u'自然语言处理', u'数据挖掘', u'搜索算法', u'精准推荐', u'用户研究员', u'交互设计师', u'.NET',
                    u'Java', u'C', u'PHP', u'Ruby', u'Node.js', u'iOS', u'Android', u'Javascript',
                    u'MongoDB', u'产品经理', u'APP设计师', u'UI设计师', u'数据分析师']

    os.chdir('./html')
    print(os.getcwdu())

    for sc in start_skills:
        download_job_details(sc)

    os.chdir('..')
    print(os.getcwdu())

    ### load job data from html files, time: 10 minutes for 9900 jobs.
    start = datetime.datetime.now()

    os.chdir('./html/detail')
    print(os.getcwd())

    detail_html_paths = []
    for skill in start_skills:
        for f in glob.glob(skill + u'_*.html'):
            hp = os.path.join(os.getcwdu(), f)
            # print(hp)
            detail_html_paths.append((skill, hp))
            # break
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
    ### load job data from html files end.

    # for k in all_jc:
    #     print(all_jc[k]['comp_name'])
    #
    # print('')
    # for k in all_comps:
    #     show_obj(all_comps[k])


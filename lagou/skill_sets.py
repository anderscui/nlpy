# coding=utf-8
from common.persistence import from_pickle, to_pickle

# job_data_file = '../crawlers/unified.pkl'
# jobs = from_pickle(job_data_file)
# print(type(jobs))


# def write_jobs_list():
#     jlist = jobs.values()
#     to_pickle(jlist, '../crawlers/unified_list.pkl')


# job_data_list_file = '../crawlers/unified_list.pkl'
# job_list = from_pickle(job_data_list_file)
# # print(type(job_list))
#
#
# def write_jobs_skill_to_file(skill, jobs, file_name):
#     jobs_skill = [j for j in jobs if j['skill_tag'] == skill]
#     print(len(jobs_skill))
#     to_pickle(jobs_skill, file_name)
#
#
# skill = u'交互设计师'
# write_jobs_skill_to_file(skill, job_list, 'ux.pkl')
#
# skill = u'自然语言处理'
# write_jobs_skill_to_file(skill, job_list, 'nlp.pkl')
#
# skill = u'数据挖掘'
# write_jobs_skill_to_file(skill, job_list, 'dm.pkl')
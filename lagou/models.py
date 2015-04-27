#!/usr/bin/env python
#encoding=utf-8
import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, Unicode, Date, Boolean, Sequence, ForeignKey
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Company(Base):
    __tablename__ = 'lagou_company'

    id = Column(Integer, Sequence('id'), primary_key=True)
    name = Column(Unicode(200))
    comp_id = Column(Integer)
    domain = Column(Unicode(200), nullable=True)
    size = Column(Unicode(50))

    url = Column(Unicode(500), nullable=True)
    logo = Column(Unicode(500), nullable=True)
    cur_stage = Column(Unicode(50), nullable=True)
    investor = Column(Unicode(200), nullable=True)
    address = Column(Unicode(500), nullable=True)

    def __unicode__(self):
        return "{0}: {1}".format(self.comp_id, self.name)


class Job(Base):
    __tablename__ = 'lagou_job'

    id = Column(Integer, Sequence('id'), primary_key=True)
    job_id = Column(Integer)
    skill_tag = Column(Unicode(200))
    title = Column(Unicode(200))
    dept = Column(Unicode(200), nullable=True)
    published_date = Column(Date)

    # request part
    salary = Column(Unicode(200))
    city = Column(Unicode(50))
    experience = Column(Unicode(200))
    education = Column(Unicode(200))
    full_time = Column(Boolean, default=True)
    benefits = Column(Unicode(500), nullable=True)

    # jd
    desc = Column(Unicode(3000))

    # comp_id = Column(Integer, ForeignKey('lagou_company.id'), nullable=False)
    # use class name
    # company = relationship('Company', backref=backref('jobs'))
    comp_id = Column(Integer)

    def __unicode__(self):
        return "{0}: {1}, comp: {2}".format(self.job_id, self.title, self.company.name)


def unified(job, comp):
    # print(comp.name)
    return {
        'job_id': job.job_id,
        'skill_tag': job.skill_tag,
        'title': job.title,
        'dept': job.dept,
        'published_date': job.published_date,

        'salary': job.salary,
        'city': job.city,
        'experience': job.experience,
        'education': job.education,
        'full_time': u'全职' if job.full_time else u'兼职',
        'benefits': job.benefits,

        'desc': job.desc,

        'comp_id': job.comp_id,
        'comp_name': comp.name,
        'domain': comp.domain,
        'size': comp.size,
        'comp_url': comp.url,
        'stage': comp.cur_stage,
        'investor': comp.investor,
        'address': comp.address
    }


if __name__ == '__main__':
    print(repr(Job.__table__))
    print(repr(Company.__table__))
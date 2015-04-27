#!/usr/bin/env python
#encoding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Job, Company

# TODO: move to global setting
echoSQL = False

engine = create_engine('sqlite:///lagou.db', echo=echoSQL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


# job dao
def add_job(job_id, title, comp):
    session = Session()
    new_job = Job(job_id=job_id, title=title, comp_id=comp.id)
    session.add(new_job)
    session.commit()


def add_books(books):
    session = Session()
    session.add_all(books)
    session.commit()


def find_job(job_id):
    session = Session()
    return session.query(Job).filter_by(job_id=job_id).first()


def job_count():
    session = Session()
    return session.query(Job).count()


# company dao
def add_company(comp_id, name):
    session = Session()
    new_comp = Company(comp_id=comp_id, name=name)
    session.add(new_comp)
    session.commit()
    return new_comp


def find_comp(comp_id):
    session = Session()
    return session.query(Company).filter_by(comp_id=comp_id).first()


if __name__ == '__main__':
    # comp = add_company(1001, u'github')
    # print job_count()
    # add_job(123, u'new job', comp)
    # print job_count()

    print(unicode(find_comp(1001)))
    print(unicode(find_job(123)))
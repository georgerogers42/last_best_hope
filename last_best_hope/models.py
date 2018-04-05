from os import environ
from contextlib import contextmanager
from datetime import datetime

import arrow

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .ejson import Encodable

try:
    DATABASE_URL = environ["DATABASE_URL"]
except KeyError:
    DATABASE_URL = "postgres://localhost/last_best_hope__dev"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)

@contextmanager
def session():
    s = Session()
    try:
        yield s
    except:
        s.rollback()
        raise
    else:
        s.commit()
    finally:
        s.close()

Base = declarative_base(bind=engine)

class Page(Base, Encodable):
    __tablename__ = "pages"
    id = Column(Integer, primary_key=True)
    slug = Column(String, nullable=False, unique=True)
    title = Column(String, nullable=False)
    contents = Column(Text, nullable=False)
    ctime = Column(DateTime, nullable=False, default=datetime.now)
    @property
    def arrow_ctime(self):
        return arrow.get(self.ctime)
    @arrow_ctime.set
    def arrow_ctime(self, o):
        self.ctime = o.datetime
    utime = Column(DateTime, nullable=False, default=datetime.now)
    @property
    def arrow_utime(self):
        return arrow.get(self.utime)
    @arrow_utime.set
    def arrow_utime(self, o):
        self.ctime = o.datetime

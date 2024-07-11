import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

import config

Base = declarative_base()


class Api(Base):
    __tablename__ = 'api'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True, nullable=False)
    url = Column(Text, nullable=False)
    create_time = Column(DateTime, default=datetime.datetime.now())


engine = create_engine(
    "mysql+pymysql://{0}:{4}@{1}:{2}/{3}".format(config.dbcfg["user"], config.dbcfg["address"],
                                                 config.dbcfg["port"],
                                                 config.dbcfg["dbname"], config.dbcfg["passwd"]),
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)
# 把表同步到数据库  （把被Base管理的所有表，都创建到数据库）
Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)

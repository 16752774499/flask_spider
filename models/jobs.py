import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

import config

Base = declarative_base()


class Jobs(Base):
    __tablename__ = 'jobs'  # 数据库表名称
    id = Column(Integer, primary_key=True)  # 生成一列，类型是Integer，主键
    jobName = Column(String(128), index=True, nullable=False, name="岗位名称")  # name列varchar32，索引，不可为空
    jobUrl = Column(Text, nullable=False, name="岗位详情")
    jobPay = Column(String(128), nullable=False, index=True, name="岗位薪资")
    jobAddress = Column(String(128), nullable=False, index=True, name="岗位地点")
    jobQualification = Column(String(128), nullable=False, index=True, name="岗位要求学历")
    jobEXP = Column(String(128), nullable=False, index=True, name="岗位要求经验")
    jobCorporation = Column(String(128), nullable=False, index=True, name="岗位公司")
    jobCorporationUrl = Column(Text, nullable=False, name="岗位公司详情")
    jobCorporationBg1 = Column(String(128), nullable=False, index=True, default="NULL", name="公司背景1")
    jobCorporationBg2 = Column(String(128), nullable=False, index=True, default="NULL", name="公司背景2")
    addTime = Column(DateTime, default=datetime.datetime.now, nullable=False)
    status = Column(String(12), default="False", index=True, nullable=False, name="查看状态")
    SearchKeyword = Column(String(32), index=True, nullable=False, name="采集时的关键字")


class Task(Base):
    __tablename__ = 'task'  # 数据库表名称
    id = Column(Integer, primary_key=True)  # 生成一列，类型是Integer，主键
    CollectionPurpose = Column(String(128), index=True, nullable=False, name="采集任务目的")
    SearchKeyword = Column(String(32), index=True, nullable=False, name="采集任务时的关键字")
    CollectionPages = Column(Integer, nullable=False, name="采集任务页数")
    CollectionCity = Column(String(128), nullable=False, name="采集任务城市")
    CollectionTarget = Column(String(128), index=True, nullable=False, name="采集任务目标")
    status = Column(String(12), default="False", index=True, nullable=False, name="采集任务状态")
    CollectionUrl = Column(Text, nullable=False, name="采集任务详情")
    CollectionType = Column(String(12), nullable=False, name="采集任务类型")
    addTime = Column(DateTime, default=datetime.datetime.now, nullable=False, name="采集任务时间")



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

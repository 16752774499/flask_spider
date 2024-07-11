import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

import config

Base = declarative_base()


class Tasks(Base):
    __tablename__ = 'tasks'  # 数据库表名称
    id = Column(Integer, primary_key=True)  # 生成一列，类型是Integer，主键
    taskId = Column(String(128), index=True, nullable=False, name="采集任务ID")
    CollectionPurpose = Column(String(128), index=True, nullable=False, name="采集任务目的")
    SearchKeyword = Column(String(32), index=True, nullable=False, name="采集任务时的关键字")
    CollectionPages = Column(String(8), nullable=False, name="采集任务页数")
    CollectionCity = Column(String(128), nullable=False, name="采集任务城市")
    CollectionTarget = Column(String(128), index=True, nullable=False, name="采集任务目标")
    status = Column(String(64), default='{"state":"Running","Msg":"正在运行"}', index=True, nullable=False, name="采集任务状态")
    CollectionUrl = Column(Text, nullable=False, name="采集任务详情")
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

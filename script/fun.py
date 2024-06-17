import json
import urllib
from datetime import date, datetime, timedelta

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

import config
from models.jobs import Jobs


def editXpath(original_string: str, start_marker: str, end_marker: str, i: int) -> str:
    # 要替换的部分的起始和结束标记
    # 新内容
    new_content = str(i)

    # 找到要替换的部分的起始和结束位置
    start_index = original_string.find(start_marker) + len(start_marker)
    end_index = original_string.find(end_marker, start_index)

    # 执行替换操作
    new_string = original_string[:start_index] + new_content + original_string[end_index:]

    return new_string


# boss方案一，重构xpath
def editBossXpath(allXpath: dict) -> dict:
    newAllXpath: dict = {}
    for k, v in allXpath.items():
        newList: list = []
        for i in v:
            replace_part = 'id("wrap")/div[2]/div[2]/div[1]/div[1]/div['
            # 替换为的新字符
            new_part = 'id("wrap")/div[2]/div[2]/div[1]/div[1]/div[1]/ul[1]/'

            # 找到要替换的部分的起始和结束位置
            start_index = i.find(replace_part)
            end_index = i.find(']/ul[1]/', start_index) + len(']/ul[1]/')

            # 执行替换操作
            new_string = i[:start_index] + new_part + i[end_index:]
            newList.append(new_string)
        newAllXpath[k] = newList
    return newAllXpath


# boss方案二,通过js注入删除影响元素提取xpath的页面元素
# /html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/div/div/div/a[10]
# /html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/a[10]
def zhilianNextUrl(url: str, pageNum: int):
    index = url.find("&p=")
    # 如果找到 "&p="，则删除该子字符串及其后面的内容
    if index != -1:
        result_string = url[:index]
        print("处理后字符串:", result_string)
        NextUrl = result_string + "&p=" + str(pageNum + 1)
        return NextUrl
    NextUrl = url + "&p=" + str(pageNum + 1)
    return NextUrl


def saveJson(fileName: str, data: str) -> bool:
    """
    将字符串格式的数据保存到json文件中。

    Args:
        fileName (str): json文件的名称，不包含后缀名。
        data (str): 需要保存的数据，字符串格式。

    Returns:
        bool: 如果保存成功返回True，否则返回False。

    """
    file_path = "saveFile/jsonFiles/" + fileName + ".json"
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        return True
    except Exception as e:
        print("{0}保存过程中出现异常：".format(file_path), e)
        return False


def setParsingRules(domain_name: str) -> str:
    if domain_name == "www.zhipin.com":
        DataList: list = [
            {"xpath": "id(\"wrap\")/div[2]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/div[1]/a[1]/div[1]/span[1]",
             "text": "岗位"},
            {"xpath": "id(\"wrap\")/div[2]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/div[1]/a[1]/div[1]/span[2]/span[1]",
             "text": "地点"},
            {"xpath": "id(\"wrap\")/div[2]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/div[1]/a[1]/div[2]/span[1]",
             "text": "薪资"},
            {"xpath": "id(\"wrap\")/div[2]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/div[1]/a[1]/div[2]/ul[1]/li[1]",
             "text": "经验"},
            {"xpath": "id(\"wrap\")/div[2]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/div[1]/a[1]/div[2]/ul[1]/li[2]",
             "text": "学历"},
            {"xpath": "id(\"wrap\")/div[2]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[1]/div[2]/h3[1]/a[1]",
             "text": "公司名"},
            {"xpath": "id(\"wrap\")/div[2]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[1]/div[2]/ul[1]/li[2]",
             "text": "公司性质"},
            {"xpath": "id(\"wrap\")/div[2]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[1]/div[2]/ul[1]/li[3]",
             "text": "公司规模"},
            {"xpath": "id(\"wrap\")/div[2]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/div[1]/a[1]",
             "text": "岗位链接"}
        ]
        return json.dumps(DataList)
    elif domain_name == "sou.zhaopin.com":
        DataList: list = [
            # //*[@id="positionList-hook"]/div/div[1]/div[1]/div[1]/div[1]/div[1]/a
            {"xpath": "id(\"positionList-hook\")/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]",
             "text": "岗位"},
            {"xpath": "id(\"positionList-hook\")/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]",
             "text": "地点"},
            {"xpath": "id(\"positionList-hook\")/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/p[1]",
             "text": "薪资"},
            {"xpath": "id(\"positionList-hook\")/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]",
             "text": "经验"},
            {"xpath": "id(\"positionList-hook\")/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]",
             "text": "学历"},
            {"xpath": "id(\"positionList-hook\")/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]",
             "text": "公司名"},
            {"xpath": "id(\"positionList-hook\")/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]",
             "text": "公司性质"},
            {"xpath": "id(\"positionList-hook\")/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]",
             "text": "公司规模"},
        ]
        return json.dumps(DataList)
    else:
        return json.dumps({"code": "10001", "message": '不在采集范围内'})


# 格式化数据（需要可视化的数据）
def formattingData(domain_name: str, data: dict) -> list:
    """
    根据给定的域名对字典数据进行格式化处理，并返回处理后的列表。

    Args:
        domain_name (str): 域名，用于确定数据格式化的方式。
        data (dict): 需要进行格式化处理的字典数据。

    Returns:
        list: 格式化处理后的列表。

    """
    dataList: list = returnList(data=data)
    if domain_name == "www.zhipin.com":

        for i, j in enumerate(dataList):
            j[1], j[10] = j[10], j[1]
            j[3], j[10] = j[10], j[3]
            j[5], j[10] = j[10], j[5]
            j[6], j[10] = j[10], j[6]
            j[7], j[10] = j[10], j[7]
            j[9], j[10] = j[10], j[9]
            j[8], j[9] = j[9], j[8]
            # print(i, j)

    elif domain_name == "sou.zhaopin.com":

        for i, j in enumerate(dataList):
            j[2], j[3] = j[3], j[2]
            j[4], j[5] = j[5], j[4]
            j[8], j[9] = j[9], j[8]

    return dataList


def returnList(data: dict) -> list:
    """
    将嵌套的字典转化为列表。

    Args:
        data (dict): 需要转化的嵌套字典。

    Returns:
        list: 转化后的列表，包含嵌套字典中所有值的扁平化结果。

    """
    tempList: list = []
    iter_data = iter(data.items())
    while True:
        try:
            K, V = next(iter_data)
            iter_V = iter(V.items())
            while True:
                try:
                    k, v = next(iter_V)
                    tempList.append(v)
                except StopIteration:
                    break
        except StopIteration:
            break
    return tempList


def insertDB(dataList: list, Keyword: str) -> None:
    session = returnDbSession()
    try:
        for i in dataList:
            job = Jobs(jobName=i[0], jobUrl=i[1], jobPay=i[2], jobAddress=i[3],
                       jobQualification=i[4],
                       jobEXP=i[5],
                       jobCorporation=i[6], jobCorporationUrl=i[7], jobCorporationBg1=i[8], jobCorporationBg2=i[9],
                       SearchKeyword=Keyword)
            session.add(job)
            session.commit()
        # 第五步：关闭session对象
        session.close()
        print("数据插入成功")
    except Exception as e:
        print("数据插入失败：{0}".format(e))


def returnDbSession() -> object:
    engine = create_engine(
        "mysql+pymysql://{0}:{4}@{1}:{2}/{3}".format(config.dbcfg["user"], config.dbcfg["address"],
                                                     config.dbcfg["port"],
                                                     config.dbcfg["dbname"], config.dbcfg["passwd"]),
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
    Session = sessionmaker(bind=engine)
    # 第三步：拿到session对象,相当于连接对象（会话）
    session = Session()
    return session


def getAreaQuantity(SearchKeyword: str) -> list:
    """
    获取西安各个区域的岗位数量

    Args:
        无

    Returns:
        list: 包含各个区域岗位数量的字典列表，每个字典包含两个键值对：
            - name (str): 区域名称，包含“区”或“县”后缀
            - value (int): 该区域的岗位数量

    """
    AreaQuantityList: list = []
    AreaQuantityDict: dict = {}
    session = returnDbSession()
    cityRegions = ["碑林", "莲湖", "新城", "未央", "灞桥", "雁塔", "周至", "鄠邑", "长安", "蓝田", "临潼", "阎良", "高陵"]
    for i in cityRegions:
        search_term = i  # 模糊搜索关键词
        if SearchKeyword == "all":
            query = session.query(Jobs).filter(
                Jobs.jobAddress.like(f'%{search_term}%'))
        else:
            query = session.query(Jobs).filter(
                Jobs.jobAddress.like(f'%{search_term}%')).filter(Jobs.SearchKeyword == SearchKeyword)
        result_count = query.count()
        AreaQuantityDict[i] = result_count
        # 打印查询到的数量
        print("{0}岗位数有{1}个！".format(i, result_count))
    session.close()

    for key, value in AreaQuantityDict.items():

        if key == "蓝田" or key == "周至":
            key += "县"
            TempAreaQuantityDict: dict = {"name": key, "value": value}
            AreaQuantityList.append(TempAreaQuantityDict)
        else:
            key += "区"
            TempAreaQuantityDict: dict = {"name": key, "value": value}
            AreaQuantityList.append(TempAreaQuantityDict)
    return AreaQuantityList


# 岗位总数目
def getJobsNums(SearchKeyword: str) -> int:
    session = returnDbSession()
    if SearchKeyword == "all":
        jobsNums: int = session.query(func.count(Jobs.id)).scalar()
    else:
        jobsNums: int = session.query(func.count(Jobs.id)).filter(Jobs.SearchKeyword == urllib.parse.unquote(SearchKeyword)).scalar()
    session.close()
    return jobsNums


# 今日更新
def toDayUpdata(SearchKeyword: str) -> int:
    """
    查询并返回当天更新到数据库的Job数量。

    Args:
        无

    Returns:
        int: 当天更新到数据库的Job数量。

    """
    today = date.today()
    session = returnDbSession()
    # 查询今日更新到数据库的内容
    if SearchKeyword == "all":
        today_count = session.query(func.count(Jobs.id)).filter(func.DATE(Jobs.addTime) == today).scalar()
    else:
        today_count = session.query(func.count(Jobs.id)).filter(func.DATE(Jobs.addTime) == today).filter(
            Jobs.SearchKeyword == urllib.parse.unquote(SearchKeyword)).scalar()
    # # 打印今日更新的内容
    # for job in updated_today:
    #     print(job.jobName)
    session.close()
    return today_count


def viewStatus(status: bool, SearchKeyword: str) -> int:
    session = returnDbSession()
    if SearchKeyword == "all":
        statusNums = session.query(func.count(Jobs.id)).filter(Jobs.status == "{0}".format(status)).scalar()
    else:
        statusNums = session.query(func.count(Jobs.id)).filter(Jobs.status == "{0}".format(status)).filter(
            Jobs.SearchKeyword == urllib.parse.unquote(SearchKeyword)).scalar()
    session.close()
    return statusNums


def latestToday(SearchKeyword: str, regName: str) -> list:
    """
    获取今日最新职位列表

    Args:
        无

    Returns:
        list: 最新职位列表，包含以下字段：
            - id (int): 职位ID
            - jobCorporation (str): 招聘公司名称
            - jobName (str): 职位名称
            - jobUrl (str): 职位链接
            - jobPay (str): 薪资范围
            - jobCorporationUrl (str): 公司链接

    """
    latestTodayList: list = []
    session = returnDbSession()
    if SearchKeyword == "all":
        if regName == "all":
            latest_records = session.query(Jobs).order_by(Jobs.id.desc()).all()
        else:
            latest_records = session.query(Jobs).order_by(Jobs.id.desc()).filter(
                Jobs.jobAddress.like(f'%{regName}%')).all()
    else:
        if regName == "all":
            latest_records = session.query(Jobs).filter(
                Jobs.SearchKeyword == urllib.parse.unquote(SearchKeyword)).order_by(Jobs.id.desc()).all()
        else:
            latest_records = session.query(Jobs).filter(
                Jobs.SearchKeyword == urllib.parse.unquote(SearchKeyword)).order_by(Jobs.id.desc()).filter(
                Jobs.jobAddress.like(f'%{regName}%')).all()
    for record in latest_records:
        # print(record.jobCorporation, record.jobName, record.jobUrl, record.jobPay)  # 打印每条记录
        latestTodayList.append(
            {"id": record.id, "jobCorporation": record.jobCorporation, "jobName": record.jobName,
             "jobUrl": record.jobUrl,
             "jobPay": record.jobPay, "jobCorporationUrl": record.jobCorporationUrl})
    print(len(latestTodayList))
    session.close()
    return latestTodayList


def changeStatus(Id: str):
    """
    更新指定 id 的 Jobs 记录中 status 字段为 "True"。

    Args:
    - Id (str): 需要更新 status 字段的 Jobs 记录的 id。

    Returns:
    - str: 更新后的 Jobs 记录的 id。

    """
    session = returnDbSession()
    # 查询指定 id 的记录
    job = session.query(Jobs).filter_by(id=Id).first()
    if job:
        # 更新 status 值
        job.status = "True"
        # 提交更改
        session.commit()
        print(f"Status value of record with id {Id} updated successfully.")
    else:
        print(f"Record with id {Id} not found.")
    # 关闭会话
    session.close()
    return Id


def setPayFormat(PayString):
    """
    根据薪资字符串计算薪资平均值。

    Args:
        PayString (str): 薪资字符串，可能包含范围（使用'-'分隔）、单位（'万'、'千'、'天'、'议'、'次'）等。

    Returns:
        Union[float, str]: 返回计算后的薪资平均值（单位为元），若无法计算则返回原薪资字符串。

    """
    # 存在“·”
    tempList1: list = []
    if "·" in PayString:
        split_list = PayString.split("·")
        # 打印分割后的结果
        for item1 in split_list:
            tempList1.append(item1)
        # 处理“·”前的薪资
        # 存在“-”
        # 去除"薪"
        tempList1[1] = tempList1[1][:-1]
        tempList2: list = []
        if "-" in tempList1[0]:
            split_list = tempList1[0].split("-")
            for item2 in split_list:
                tempList2.append(item2)
            # 如果-前后两个字符串结尾不一样且后面字符串结尾为K时
            if (tempList2[0][-1] != tempList2[1][-1]) and tempList2[1][-1] == "K":
                tempList2[1] = tempList2[1][:-1]
                Pay = round((((int(tempList2[0]) + int(tempList2[1])) / 2) * int(tempList1[1])) / 12, 1) * 1000
                return Pay
            # 都为万
            if tempList2[0][-1] == tempList2[1][-1] == "万":
                tempList2[0] = int(float(tempList2[0][:-1]) * 10000)
                tempList2[1] = int(float(tempList2[1][:-1]) * 10000)
                Pay = round((((int(tempList2[0]) + int(tempList2[1])) / 2) * int(tempList1[1])) / 12, 1)
                return Pay
                # 都为千
            elif tempList2[0][-1] == tempList2[1][-1] == "千":
                tempList2[0] = int(float(tempList2[0][:-1]) * 1000)
                tempList2[1] = int(float(tempList2[1][:-1]) * 1000)
                Pay = round((((int(tempList2[0]) + int(tempList2[1])) / 2) * int(tempList1[1])) / 12, 1)
                return Pay
            # 前为千,后为万
            elif (tempList2[0][-1] != tempList2[1][-1]) and (tempList2[0][-1] == "千" and tempList2[1][-1] == "万"):
                tempList2[0] = int(float(tempList2[0][:-1]) * 1000)
                tempList2[1] = int(float(tempList2[1][:-1]) * 10000)
                Pay = round((((int(tempList2[0]) + int(tempList2[1])) / 2) * int(tempList1[1])) / 12, 1)
                return Pay
    # elif PayString[:-1] == "天" or PayString[:-1] == "议" or PayString[:-1] == "次":
    elif "天" in PayString or "议" in PayString or "次" in PayString or "/" in PayString:
        return PayString
    else:
        tempList2: list = []
        if "-" in PayString:
            split_list = PayString.split("-")
            for item2 in split_list:
                tempList2.append(item2)
            # 如果-前后两个字符串结尾不一样且后面字符串结尾为K时
            if (tempList2[0][-1] != tempList2[1][-1]) and tempList2[1][-1] == "K":
                tempList2[1] = tempList2[1][:-1]
                Pay = round(((int(tempList2[0]) + int(tempList2[1])) / 2), 1) * 1000
                return Pay
            # 都为万
            if tempList2[0][-1] == tempList2[1][-1] == "万":
                tempList2[0] = int(float(tempList2[0][:-1]) * 10000)
                tempList2[1] = int(float(tempList2[1][:-1]) * 10000)
                Pay = round(((int(tempList2[0]) + int(tempList2[1])) / 2), 1)
                return Pay
                # 都为千
            elif tempList2[0][-1] == tempList2[1][-1] == "千":
                tempList2[0] = int(float(tempList2[0][:-1]) * 1000)
                tempList2[1] = int(float(tempList2[1][:-1]) * 1000)
                Pay = round(((int(tempList2[0]) + int(tempList2[1])) / 2), 1)
                return Pay
            # 前为千,后为万
            elif (tempList2[0][-1] != tempList2[1][-1]) and (tempList2[0][-1] == "千" and tempList2[1][-1] == "万"):
                tempList2[0] = int(float(tempList2[0][:-1]) * 1000)
                tempList2[1] = int(float(tempList2[1][:-1]) * 10000)
                Pay = round(((int(tempList2[0]) + int(tempList2[1])) / 2), 1)
                return Pay


def getSearchKeywordClass() -> list:
    ClassList: list = []
    session = returnDbSession()

    distinct_search_keywords = session.query(Jobs.SearchKeyword).distinct().all()

    # 打印不同的 SearchKeyword 值
    for keyword in distinct_search_keywords:
        print(keyword[0])
        ClassList.append(keyword[0])
    # 关闭会话
    session.close()
    return ClassList


def returnClassList() -> list:
    """
    获取所有职位分类和对应数量

    Args:
        无参数

    Returns:
        list: 包含两个列表的列表，第一个列表为所有职位分类，第二个列表为对应职位分类的数量

    """
    classListNums: list = []
    session = returnDbSession()
    classList = getSearchKeywordClass()
    for item in classList:
        count = session.query(Jobs).filter(Jobs.SearchKeyword == item).count()
        classListNums.append(count)
    session.close()
    return [classList, classListNums]


def WeeklyDataVolumeList() -> list:
    """
    获取近一周内每天入库的数据量列表。

    Args:
        无参数。

    Returns:
        list: 包含两个列表的列表，第一个列表为近一周内每天的格式化日期（'YYYY-MM-DD'格式），第二个列表为对应日期的入库数据量。

    """
    session = returnDbSession()
    one_week_ago = datetime.now().date() - timedelta(days=7)
    all_dates = [one_week_ago + timedelta(days=i) for i in range(8)]  # 一周内所有日期，包括一周前的日期

    # 查询近一周内每天入库的数据量
    result = session.query(func.date(Jobs.addTime), func.count(Jobs.id)) \
        .filter(Jobs.addTime >= one_week_ago) \
        .group_by(func.date(Jobs.addTime)) \
        .all()

    # 将查询结果转换为字典，方便后续处理
    data_dict = {date: count for date, count in result}

    # 生成包含所有日期的数据量列表和格式化日期列表
    data_list = [data_dict.get(date, 0) for date in all_dates]
    formatted_dates = [date.strftime('%Y-%m-%d') for date in all_dates]  # 格式化日期为 'YYYY-MM-DD' 格式

    # 输出格式化后的日期列表和数据量列表
    print("日期列表:", formatted_dates)
    print("数据量列表:", data_list)
    return [formatted_dates, data_list]

# https://www.zhipin.com/web/geek/job?query=&city=101110100&position=100101&page=1
# https://www.zhipin.com/web/geek/job?query=&city=101110100&position=100101&page=2


# //*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[2]/ul/li[1]/div[1]/a/div[2]/ul/li[1]
# //*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[2]/ul/li[1]/div[1]/a/div[2]/ul/li[2]


# id("wrap")/div[2]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[1]/div[2]/h3[1]/a[1]
# id("wrap")/div[2]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[2]/div[1]/div[1]/div[2]/h3[1]/a[1]
import json
import re
from spider import spider
from script import fun


def outPageUrl(url: str, page_num: int) -> list:
    urlList: list = []
    for i in range(1, page_num + 1):
        # 将字符串分割成两部分
        url_parts = (url + "&page=1").rsplit("=", 1)
        # 构建新的URL
        new_url = url_parts[0] + "=" + str(i)
        urlList.append(new_url)

    return urlList


# id("wrap")/div[2]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/div[2]/ul[1]/li[3]
# 解析参数,全部替换为第一条
def ParseParameters(domain_name: str, url: str, XpathList: str, page_num: int) -> dict:
    # 检查数据第几列
    # 构造每一条xpath
    allXpath: dict = {}
    for i in range(1, 31):
        dirID: str = "dom_" + str(i)
        temp_list: list = []
        for j in json.loads(XpathList):

            replaced_text = fun.editXpath(original_string=j["xpath"],
                                          start_marker='id("wrap")/div[2]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[',
                                          end_marker=']/div', i=i)
            temp_list.append(replaced_text)
        allXpath[dirID] = temp_list
    # print(allXpath)
    return spider.work(url=url, allXpath=allXpath, domain_name=domain_name, page_num=page_num)


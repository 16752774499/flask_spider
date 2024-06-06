# https://sou.zhaopin.com/?jl=854&kw=Java%E5%BC%80%E5%8F%91&p=1

import json
import re
from spider import spider
from script import fun


def ParseParameters(domain_name: str, url: str, XpathList: str, page_num: int) -> dict:
    # 检查数据第几列
    # 构造每一条xpath
    allXpath: dict = {}
    for i in range(1, 31):
        dirID: str = "dom_" + str(i)
        temp_list: list = []
        for j in json.loads(XpathList):
            replaced_text = fun.editXpath(original_string=j["xpath"],
                                          start_marker='id("positionList-hook")/div[1]/div[',
                                          end_marker=']/div', i=i)
            temp_list.append(replaced_text)
        allXpath[dirID] = temp_list
    # print(allXpath)
    return spider.work(url=url, allXpath=allXpath, domain_name=domain_name, page_num=page_num)

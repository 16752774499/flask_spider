# 通过自动话实现翻页

import json
import re
from spider import spider
from script import fun


# 20条每页
def ParseParameters(domain_name: str, url: str, XpathList: str, page_num: int) -> dict:
    # 构造每一条xpath
    allXpath: dict = {}
    for i in range(1, 21):
        dirID: str = "dom_" + str(i)
        temp_list: list = []
        for j in json.loads(XpathList):
            replaced_text = fun.editXpath(original_string=j["xpath"],
                                          start_marker='id("app")/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[',
                                          end_marker=']/div', i=i)
            temp_list.append(replaced_text)
        allXpath[dirID] = temp_list
    # print(allXpath)

    return spider.work(url=url, allXpath=allXpath, domain_name=domain_name, page_num=page_num)

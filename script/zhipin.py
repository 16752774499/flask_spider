# https://sou.zhaopin.com/?jl=854&kw=Java%E5%BC%80%E5%8F%91&p=1

import json

from script import fun
from spider import spider


def ParseParameters(domain_name: str, url: str, XpathList: str, page_num: int) -> tuple:
    # 检查数据第几列
    # 构造每一条xpath
    allXpath: dict = {}
    for i in range(1, 21):
        dirID: str = "dom_" + str(i)
        temp_list: list = []
        for j in json.loads(XpathList):
            # //*[@id="positionList-hook"]/div/div[1]/div[2]/div[1]/div[1]/div[1]/a
            replaced_text = fun.editXpath(original_string=j["xpath"],
                                          start_marker='id("positionList-hook")/div[1]/div[1]/div[',
                                          end_marker=']/div', i=i)
            temp_list.append(replaced_text)
        allXpath[dirID] = temp_list
    # print(allXpath)
    return spider.work(url=url, allXpath=allXpath, domain_name=domain_name, page_num=page_num)

# 傻逼智联
# 隐藏页面元素
# /html/body/div/div[4]/div[2]/div[2]/div/div[1]/div[1]  第一页
# /html/body/div/div[4]/div[2]/div[2]/div/div[1]/div[1] 第二页
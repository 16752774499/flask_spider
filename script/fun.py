import json


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
    file_path = "saveFile/jsonFiles/" + fileName + ".json"
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        return True
    except Exception as e:
        print("{0}保存过程中出现异常：".format(file_path), e)
        return False


def getShowData(url: str, pageNum: int) -> list:
    pass


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
        return "sou.zhaopin.com"

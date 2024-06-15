import time

from selenium import webdriver
# from DrissionPage import ChromiumPage
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from script import fun


def work(url: str, allXpath: dict, domain_name: str, page_num: int) -> dict:
    # 创建Chrome浏览器实例
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(8)
    # 设置隐式等待时间为 10 秒
    driver.implicitly_wait(5)
    if domain_name == "www.zhipin.com":
        # //*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/a[10]
        # 处理boos页面xpath不统一
        Data: dict = {}
        for num in range(page_num):
            print(num)
            pageId = "page_" + str(num + 1)
            if num == 0:
                NextButton = driver.find_element(By.CLASS_NAME, "ui-icon-arrow-right")
                Data[pageId] = task(driver=driver, allXpath=allXpath, NextButton=NextButton, domain_name=domain_name,
                                    pageNum=(num + 1), url=url)
            else:
                NextButton = driver.find_element(By.CLASS_NAME, "ui-icon-arrow-right")
                Data[pageId] = task(driver=driver, allXpath=fun.editBossXpath(allXpath=allXpath), NextButton=NextButton,
                                    domain_name=domain_name, pageNum=(num + 1), url=url)
        driver.quit()
        return Data
    elif domain_name == "we.51job.com":
        Data: dict = {}
        for num in range(page_num):
            time.sleep(1)
            script = """
                     var elements = document.querySelectorAll('div.icon_promotion');
                     elements.forEach(function(element) {
                        element.remove();
                     });
                    """
            driver.execute_script(script)
            pageId = "page_" + str(num + 1)
            NextButton = driver.find_element(By.CLASS_NAME, "btn-next")
            Data[pageId] = task(driver=driver, allXpath=allXpath, NextButton=NextButton, domain_name=domain_name,
                                pageNum=(num + 1), url=url)
        driver.quit()
        return Data
    elif domain_name == "sou.zhaopin.com":

        Data: dict = {}
        for num in range(page_num):
            # 第一页手动登录
            if num == 0:

                script = """
                    var textBox = document.createElement('input');

                    // 设置文本框的类型为文本框
                    textBox.type = 'text';
                    
                    // 设置文本框的初始值为 "false"
                    textBox.value = '显示表示未登录';
                    
                    // 添加类名 "isLogin" 到文本框
                    textBox.className = 'xiaohua';
                    
                    // 将文本框元素添加到文档的 body 元素中，即网页最底部
                    document.body.appendChild(textBox);
                    const loginBtn = document.querySelector('.login-btn');
                    loginBtn.click();
                              
                """
                driver.execute_script(script)
                while 1:
                    try:
                        state = driver.find_element(By.CLASS_NAME, "xiaohua")
                        print("标记未消失！")
                        continue
                    except NoSuchElementException:
                        print("标记消失，已经登录")
                        break
            pageId = "page_" + str(num + 1)
            Data[pageId] = task(driver=driver, allXpath=allXpath, NextButton=None, domain_name=domain_name,
                                pageNum=(num + 1), url=url)

        driver.quit()
        return Data
    else:
        Data: dict = {"response": "该域名未在采集名单！"}
        return Data


def task(driver, allXpath: dict, NextButton: object, domain_name: str, pageNum: int, url: str) -> dict:
    time.sleep(3)
    data_obj: dict = {}
    for k, v in allXpath.items():
        # print(v)
        temp_list: list = []
        for i in v:
            try:

                element = driver.find_element(By.XPATH, i)
                detailsUrl = element.get_attribute("href")
                text = element.text
                temp_list.append(text)
                if detailsUrl is None:
                    pass
                else:
                    temp_list.append(detailsUrl)
            except NoSuchElementException:
                print(r"无法定位到该元素或该元素不存在：{0}".format(i))
                temp_list.append("NULL")

                continue
        data_obj[k] = temp_list
    print(data_obj)
    if domain_name == "sou.zhaopin.com":
        # 智联按钮不可正常跳转
        # 处理智联url
        driver.get(fun.zhilianNextUrl(url=url, pageNum=pageNum))
    else:
        NextButton.click()
    time.sleep(3)

    return data_obj

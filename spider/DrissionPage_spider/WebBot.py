# https://www.zhipin.com/web/geek/job?query=Java&city=101110500&experience=108&degree=206&scale=301&stage=801&jobType=1901&salary=404

import time

from DrissionPage import WebPage


class WebBot:

    def __init__(self, query: str = None, city: str = None, experience: str = None, degree: str = None,
                 scale: str = None, stage: str = None, salary: str = None, nums: int = 10):
        """
        初始化方法，创建一个用于筛选职位信息的对象。

        Args:
            query (str, optional): 职位查询关键词，如 "Python工程师". 默认为None.
            city (str, optional): 职位所在城市，如 "北京". 默认为None.
            experience (str, optional): 职位要求的工作经验，如 "1-3年". 默认为None.
            degree (str, optional): 职位要求的学历，如 "本科". 默认为None.
            scale (str, optional): 公司规模，如 "500-2000人". 默认为None.
            stage (str, optional): 公司融资阶段，如 "B轮". 默认为None.
            salary (str, optional): 职位薪资范围，如 "15k-30k". 默认为None.

        Returns:
            None: 该方法不返回任何值，用于初始化对象。

        """
        self.query = query
        self.city = city
        self.experience = experience
        self.degree = degree
        self.scale = scale
        self.stage = stage
        self.salary = salary
        self.nums = nums
        self.WebBot = WebPage()
        # 洗过的数据
        self.DATA: list = []

    def buildUrl(self):
        # 不为空的参数拼接，为空不拼接
        url = "https://www.zhipin.com/web/geek/job?"
        if self.query:
            url += f"query={self.query}&"
        if self.city:
            url += f"city={self.city}&"
        if self.experience:
            url += f"experience={self.experience}&"
        if self.degree:
            url += f"degree={self.degree}&"
        if self.scale:
            url += f"scale={self.scale}&"
        if self.stage:
            url += f"stage={self.stage}&"
        if self.salary:
            url += f"salary={self.salary}&"
        return url

    def buildUrlList(self):
        url = self.buildUrl()
        # 生成url列表
        return [url + f"page={i}" for i in range(1, self.nums + 1)]

    def listenApi(self, listenApiName: str = 'zpgeek/search/joblist.json'):
        self.WebBot.listen.start(listenApiName)
        for url in self.buildUrlList():
            self.WebBot.get(url)
            time.sleep(0.5)
            res = self.WebBot.listen.wait().response.body
            if res['message'] == 'Success':
                self.cleanseData(res['zpData']['jobList'])

    # 数据处理
    def cleanseData(self, data: list):

        if data is None:
            return
        self.DATA.extend(data)

    def returnData(self):
        return self.DATA

    def __del__(self):
        """
        退出浏览器，释放资源。
        Returns:
            None: 该方法不返回任何值，用于退出浏览器。
        """
        print("退出浏览器")
        self.WebBot.close()

# abot = WebBot(query="Java", city="100010000", nums=3)
# abot.cleanseData(abot.listenApi())
# print(abot.returnData())
# del abot

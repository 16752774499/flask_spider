import json
import random
import smtplib
from datetime import datetime
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests

emailCfg: dict = {
    "emailUser": "wyx20021009@163.com",
    "emailPasswd": "UFHMNQOSRQAJPYUX",
    "emailHost": "smtp.163.com",
    "emailPort": 25,
    "emailSender": "wyx20021009@163.com",
}


def getMsg(key: str) -> str:
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    # 获取当前日期
    today = datetime.today()

    # 将日期转换为整数形式
    seed = int(today.strftime('%Y%m%d'))

    # 设置随机数种子
    # random.seed(seed)
    # JH4ceb70486ceedb30014807dcccad510c
    # MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEA6jt4iPDyyK5pDqGDVbpJSThFXMkgG7eS0wbslACPpoy1b31XjbrHDRSD6KX8IeAeuHNuY+v8npGqqEjgI97H9VF/k7qoKjp+CMi+kWq7xUpPyXzwSXaHKuNZKD0Al+3va9QUvbswwYefNYoPk2G3whR+DrxCceBdKOkhhakOL5NN64LP86TemJCnyec0g2Nmp0YFlW1B+xZgsxEDs8ikW2RVSBWf6oAnfXSSj5TzOjkdwXbUhpobOELG3XW3KcDRYp9BSSFjG9zV7TxyumvjjZMJ1QsOnQbEuKlsTC6jdVTqWlFrkQY6/nO5+0+IN8DEhnXypPQLL/XS63GzuVlNJyjtEHjaJ1dvJc+KinPXPTTRd+x1dXyykJLY8iT69aUwID7RcTdHEoR65lUdm8cyQGqOE5mRkE4FZkad61aaKChy5dQeYqGOKM8Z61AVpqG1yvX31YCcKyZC/Fq2OQHbB3npHTSFC2XpxYWWZbsIa4l24iscpRl3gGbE7Dnmwp5XAgMBAAE=
    response = requests.get(
        "http://v.juhe.cn/joke/content/text.php?page={0}&pagesize={1}&key={2}".format(random.randint(0, 5),
                                                                                      random.randint(0, 5), key),
        headers=header)
    msg = response.text
    print(json.loads(msg)["result"]["data"][0]["content"])
    return json.loads(msg)["result"]["data"][0]["content"]


def sendEmail(mailCfg: dict, msgData: str, receivers: list):  # 创建邮件对象
    """
    发送邮件

    Args:
        mailCfg (dict): 邮件配置信息，包含以下键值对
            - emailSender (str): 发送者邮箱地址
            - emailHost (str): SMTP服务器地址
            - emailPort (int): SMTP服务器端口号
            - emailUser (str): 发送者邮箱用户名
            - emailPasswd (str): 发送者邮箱密码

    Returns:
        None

    """
    errorList: list = []
    for item in receivers:
        try:
            # 创建一个带附件的实例
            message = MIMEMultipart()
            message['From'] = mailCfg["emailSender"]
            message['To'] = item["receivers"]
            subject = '😀'
            message['Subject'] = Header(subject, 'utf-8')
            mail_msg = r'''
                        <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Title</title>
                <style>
                    .container {{
                        width: 80%; /* 设置容器宽度 */
                        text-align: center; /* 水平居中显示 */
                        margin: 0 auto; /* 可选：设置上下居中 */
                    }}

                    .flip-card {{
                        background-color: transparent;
                        width: 200px;
                        height: 400px;
                        perspective: 1000px;
                        fonts-family: sans-serif;
                    }}

                    .title {{
                        fonts-size: 1.0em;
                        fonts-weight: 900;
                        text-align: center;
                        margin: 0;
                    }}

                    .flip-card-inner {{
                        position: relative;
                        width: 130%;
                        height: 100%;
                        text-align: center;
                        transition: transform 0.8s;
                        transform-style: preserve-3d;
                        margin-top: 10px;
                    }}

                    .flip-card:hover .flip-card-inner {{
                        transform: rotateY(180deg);
                    }}

                    .flip-card-front, .flip-card-back {{
                        box-shadow: 0 8px 14px 0 rgba(0, 0, 0, 0.2);
                        position: absolute;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        width: 100%;
                        height: 100%;
                        -webkit-backface-visibility: hidden;
                        backface-visibility: hidden;
                        border: 1px solid coral;
                        border-radius: 1rem;
                    }}

                    .flip-card-front {{
                        background: linear-gradient(120deg, bisque 60%, rgb(255, 231, 222) 88%,
                        rgb(255, 211, 195) 40%, rgba(255, 127, 80, 0.603) 48%);
                        color: coral;
                    }}

                    .flip-card-back {{
                        background: linear-gradient(120deg, rgb(255, 174, 145) 30%, coral 88%,
                        bisque 40%, rgb(255, 185, 160) 78%);
                        color: white;
                        transform: rotateY(180deg);
                    }}
                </style>
            </head>
            <body>

            <div class="flip-card container">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <p class="title">亲爱的{0}，一日不见，如隔二十四小时。</p>
                        <p>不知没有我在你身边的你过的怎样。
                            不论怎样，祝你早安，午安还有晚安。</p>
                        <img src="https://img5.mtime.cn/pi/2019/05/17/154927.41853834_1000X1000.jpg">
                        <h4>-></h4>
                    </div>

                    <div class="flip-card-back">
                        <p class="title">给爷笑😀</p>
                        <p style="fonts-size: 13px">
                            有一对年轻的男女正坐在一起谈恋爱，突然女的想放屁，但这种场合怎能。于是女的想了个办法，就对男的说：哎，你听过布谷鸟的叫声吗？男的莫名其妙地说：没听过。女的马上说：那我学给你听听，就是……布……谷……她喊着，同时放屁，想用叫声掩盖放屁声。过后，女的舒服多了，就问男的：怎样？知道布谷鸟的叫声了吧？男的红着脸为难地说：……嗯，对不起……我没听见……咦？为什么？因为……因为你那放屁声太大了，所以弄得我听不见你哪布谷鸟的叫声……</p>
                        <img style="width: 100%;height: 30%" src="https://q8.itc.cn/q_70/images03/20240227/a3f370582a2243ecb2342fdd0db1b1e9.jpeg">
                    </div>
                </div>
            </div>
            </body>
            </html>
                        '''
            # 邮件正文内容
            msg = mail_msg.format(item["name"])
            message.attach(MIMEText(msg, 'html', 'utf-8'))

            try:
                smtpObj = smtplib.SMTP()
                smtpObj.connect(mailCfg["emailHost"], mailCfg["emailPort"])  # 25 为 SMTP 端口号
                smtpObj.login(mailCfg["emailUser"], mailCfg["emailPasswd"])
                smtpObj.sendmail(mailCfg["emailSender"], item["receivers"], message.as_string())
                print("邮件发送成功,user:{0}".format(item["name"]))
            except smtplib.SMTPException as e:
                print("Error: 无法发送邮件", e)
        except Exception as e:
            errorMsg = "Error: 向{0}发送失败,失败原因{1}".format(item["name"], e)
            print(errorMsg)
            errorList.append(errorMsg)


# 1754995488@qq.com 飞
# 3497379385@qq.com 小邱
# 2424940439@qq.com 轮
if __name__ == '__main__':
    sendList: list = [{"receivers": "2755319956@qq.com", "name": "小花"},
                      {"receivers": "1754995488@qq.com", "name": "飞"},
                      {"receivers": "3497379385@qq.com", "name": "小邱"},
                      {"receivers": "2424940439@qq.com", "name": "轮"}]
    sendEmail(emailCfg, None, sendList)

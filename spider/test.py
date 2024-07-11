from selenium import webdriver

# 启动浏览器
driver = webdriver.Chrome()

# 打开网页
driver.get("https://sou.zhaopin.com")

# 定义要执行的JavaScript代码
js_code = """

"""

# 执行JavaScript并获取返回值
result = driver.execute_script(js_code)
print("页面标题是：", result)

# 关闭浏览器
driver.quit()

import json
import urllib.parse

from flask import *
from flask import jsonify

from script import boss
from script import fun
from script import job_51
from script import zhipin
from script.fun import setPayFormat

# 创建蓝图对象
routes_module = Blueprint('Routes', __name__)


@routes_module.route('/', methods=["GET"])
def hello_world():  # put application's cod e here
    # 没有get请求参数时跳转/?class=all
    if request.args == {}:
        return redirect('/?class=all&reg=all')
    else:
        SearchKeyword = urllib.parse.quote(request.args.get('class'))
        print(SearchKeyword)
        regName = request.args.get('reg')
        if not SearchKeyword or SearchKeyword == "" or SearchKeyword == "undefined":
            SearchKeyword = "all"
        if not regName or regName == "" or regName == "undefined":
            regName = "all"
        print(SearchKeyword)
        # 总岗位数
        jobNums = fun.getJobsNums(SearchKeyword)
        # 今日更新
        toDayUpdate = fun.toDayUpData(SearchKeyword)
        # 查看过的数目
        statusTrueNums = fun.viewStatus(True, SearchKeyword)
        # 今日最新
        latestToday = fun.latestToday(SearchKeyword, regName)
        # 分类
        classList = fun.getSearchKeywordClass()
        # 薪资格式化
        setPayFormat(SearchKeyword)

        return render_template('index.html', jobNums=jobNums, toDayUpdate=toDayUpdate, statusTrueNums=statusTrueNums,
                               latestToday=latestToday, setPayFormat=setPayFormat, classList=classList,
                               SearchKeyword=SearchKeyword, urllib=urllib)


@routes_module.route('/browser_args', methods=["GET", "POST"])
def browser_args():
    if request.method == "GET":
        data = {"code": "10000", "message": "Success"}
        return jsonify(data)
    if request.method == "POST":
        print(request.form.get('DataList'))
        domain_name = request.form.get('domain_name')
        url = request.form.get('url')
        page_num = request.form.get('page_num')
        DataList = request.form.get('DataList')
        print(DataList)
        if domain_name == "we.51job.com":
            print("处理51——job!")
            print(DataList)
            return json.dumps(job_51.ParseParameters(domain_name, url, DataList, int(page_num)))

        elif domain_name == "sou.zhaopin.com":
            return json.dumps(zhipin.ParseParameters(domain_name, url, DataList, int(page_num)))


        elif domain_name == "www.zhipin.com":
            return json.dumps(boss.ParseParameters(domain_name, url, DataList, int(page_num)))
        else:
            print("域名不在采集范围之内，请检查！")
            return {"message": "域名不在采集范围之内，请检查！", "code": 10001}


# saveJson
@routes_module.route('/saveJson', methods=["POST"])
def saveJson():
    fileName = request.form.get('filename')
    jsonData = request.form.get('data')
    # pprint(jsonData)
    fun.saveJson(fileName=fileName, data=jsonData)
    return json.dumps({"code": "10000", "message": "Success"})


@routes_module.route('/saveExcel', methods=["POST"])
def saveExcel():
    if 'file' not in request.files:
        return json.dumps({"code": "10001", "message": 'No file part'})
    file = request.files['file']
    fileName = request.form.get('fileName')
    file.save('saveFile/excelFiles/{0}'.format(fileName) + ".xlsx")  # 保存上传的文件
    return json.dumps({"code": "10000", "message": "Success"})


# 可视化格式信息采集
@routes_module.route('/visualizeData', methods=["POST"])
def visualizeData():
    domain_name = request.form.get('domain_name')
    url = request.form.get('url')
    page_num = request.form.get('page_num')
    Keyword = request.form.get('Keyword')
    taskId = request.form.get('taskId')
    if fun.insertDbTask(formParams=request.form):
        pass
    else:
        json.dumps({"code": "10001", "message": 'tasks数据库插入失败！'})
    if domain_name == "www.zhipin.com":
        data, state = fun.formattingData(domain_name=domain_name,
                                         data=boss.ParseParameters(domain_name=domain_name, url=url,
                                                                   page_num=int(page_num),
                                                                   XpathList=fun.setParsingRules(
                                                                       domain_name=domain_name)))
        if state:
            if fun.insertDBJobs(data, Keyword):
                # 任务正常完成
                fun.modifyTaskState(True, taskId)
                fun.pushMsg(title=taskId, content="ID:{0}正常完成".format(taskId))
                return json.dumps(data)

            else:
                fun.modifyTaskState(False, taskId, "jobs数据库插入失败！")
                fun.pushMsg(title=taskId, content="{0}数据库插入失败！".format(taskId))
                return json.dumps({"code": "10001", "message": "jobs数据库插入失败！"})
        else:
            fun.modifyTaskState(False, taskId, "采集任务发生错误！")
            return json.dumps({"code": "10001", "message": "{0}采集任务发生错误,具体原因请查看微信消息推送！".format(taskId)})

    elif domain_name == "sou.zhaopin.com":
        data, state = fun.formattingData(domain_name=domain_name,
                                         data=zhipin.ParseParameters(domain_name=domain_name, url=url,
                                                                     page_num=int(page_num),
                                                                     XpathList=fun.setParsingRules(
                                                                         domain_name=domain_name)))
        if state:
            if fun.insertDBJobs(data, Keyword):
                # 任务正常完成
                fun.modifyTaskState(True, taskId)
                fun.pushMsg(title=taskId, content="ID:{0}正常完成".format(taskId))
                return json.dumps(data)
            else:
                fun.modifyTaskState(False, taskId, "jobs数据库插入失败！")
                fun.pushMsg(title=taskId, content="{0}数据库插入失败！".format(taskId))
                return json.dumps({"code": "10001", "message": "jobs数据库插入失败！"})
        else:
            fun.modifyTaskState(False, taskId, "采集任务发生错误！")
            return json.dumps({"code": "10001", "message": "{0}采集任务发生错误,具体原因请查看微信消息推送！".format(taskId)})
    else:
        return json.dumps({"code": "10001", "message": "不在采集范围内"})


# 区域数量
@routes_module.route('/AreaQuantity', methods=["GET"])
def AreaQuantity():
    SearchKeyword = request.args.get('class')
    if not SearchKeyword or SearchKeyword == "null":
        SearchKeyword = "all"
    AreaQuantityAll = fun.getAreaQuantity(SearchKeyword)
    return json.dumps(AreaQuantityAll)


@routes_module.route('/changeStatus', methods=["GET"])
def changeStatus():
    fun.changeStatus(request.args.get('id'))
    return json.dumps({"code": "10000", "message": "Success"})


@routes_module.route('/xueLi', methods=["GET"])
def xueLi():
    return fun.xueLi()

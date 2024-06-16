import json
from script.fun import setPayFormat
from flask import *
from flask_cors import *
from flask import jsonify
# from pprinty import pprint
from script import boss
from script import job_51
from script import zhipin
from script import fun

app = Flask(__name__)

app.config['DEBUG'] = True

CORS(app, supports_credentials=True)


@app.route('/', methods=["GET"])
def hello_world():  # put application's cod e here
    # class类型
    SearchKeyword = request.args.get('class')
    if not SearchKeyword or SearchKeyword == "":
        SearchKeyword = "all"
    print(SearchKeyword)
    # 总岗位数
    jobNums = fun.getJobsNums(SearchKeyword)
    # 今日更新
    toDayUpdate = fun.toDayUpdata(SearchKeyword)
    # 查看过的数目
    statusTrueNums = fun.viewStatus(True, SearchKeyword)
    # 今日最新
    latestToday = fun.latestToday(SearchKeyword)
    # 分类
    classList = fun.getSearchKeywordClass()
    # 薪资格式化
    setPayFormat(SearchKeyword)
    return render_template('index.html', jobNums=jobNums, toDayUpdate=toDayUpdate, statusTrueNums=statusTrueNums,
                           latestToday=latestToday, setPayFormat=setPayFormat, classList=classList,
                           SearchKeyword=SearchKeyword)


@app.route('/browser_args', methods=["GET", "POST"])
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
@app.route('/saveJson', methods=["POST"])
def saveJson():
    fileName = request.form.get('filename')
    jsonData = request.form.get('data')
    # pprint(jsonData)
    fun.saveJson(fileName=fileName, data=jsonData)
    return json.dumps({"code": "10000", "message": "Success"})


@app.route('/saveExcel', methods=["POST"])
def saveExcel():
    if 'file' not in request.files:
        return json.dumps({"code": "10001", "message": 'No file part'})
    file = request.files['file']
    fileName = request.form.get('fileName')
    file.save('saveFile/excelFiles/{0}'.format(fileName) + ".xlsx")  # 保存上传的文件
    return json.dumps({"code": "10000", "message": "Success"})


# 可视化格式信息采集
@app.route('/visualizeData', methods=["POST"])
def visualizeData():
    domain_name = request.form.get('domain_name')
    url = request.form.get('url')
    page_num = request.form.get('page_num')
    Keyword = request.form.get('Keyword')
    if domain_name == "www.zhipin.com":
        data = fun.formattingData(domain_name=domain_name,
                                  data=boss.ParseParameters(domain_name=domain_name, url=url, page_num=int(page_num),
                                                            XpathList=fun.setParsingRules(domain_name=domain_name)))
        fun.insertDB(data, Keyword)
        return json.dumps(data)

    elif domain_name == "sou.zhaopin.com":
        data = fun.formattingData(domain_name=domain_name,
                                  data=zhipin.ParseParameters(domain_name=domain_name, url=url, page_num=int(page_num),
                                                              XpathList=fun.setParsingRules(domain_name=domain_name)))
        fun.insertDB(data, Keyword)
        return json.dumps(data)
    else:
        return json.dumps({"code": "10001", "message": '不在采集范围内'})


# 区域数量
@app.route('/AreaQuantity', methods=["GET"])
def AreaQuantity():
    SearchKeyword = request.args.get('class')
    if not SearchKeyword or SearchKeyword == "null":
        SearchKeyword = "all"
    AreaQuantityAll = fun.getAreaQuantity(SearchKeyword)
    return json.dumps(AreaQuantityAll)


@app.route('/changeStatus', methods=["GET"])
def changeStatus():

    fun.changeStatus(request.args.get('id'))
    return json.dumps({"code": "10000", "message": "Success"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

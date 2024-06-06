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


@app.route('/')
def hello_world():  # put application's cod e here
    return 'Hello World!'


@app.route('/browser_args', methods=["GET", "POST"])
def browser_args():
    if request.method == "GET":
        data = {"code": "10000", "message": "Success"}
        return jsonify(data)
    if request.method == "POST":
        print("post请求！")
        domain_name = request.form.get('domain_name')
        url = request.form.get('url')
        page_num = request.form.get('page_num')
        DataList = request.form.get('DataList')
        if domain_name == "we.51job.com":
            print("处理51——job!")
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
    file.save('saveFile/excelFiles/{0}'.format(fileName)+".xlsx")  # 保存上传的文件
    return json.dumps({"code": "10000", "message": "Success"})


if __name__ == '__main__':
    app.run()

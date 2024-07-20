from flask import *
from flask_cors import *
from flask_restful import Api

from routes import Routes
from routes import adminRoutes
from script import fun

app = Flask(__name__)

app.config['DEBUG'] = False

CORS(app, supports_credentials=True)
api = Api(app)
# 注册路由
app.register_blueprint(Routes.routes_module)
app.register_blueprint(adminRoutes.routes_module)


# 自定义出错处理页面
@app.errorhandler(404)
def page_not_found(e):
    # 渲染404错误页面，并传递msg和state参数
    return render_template('404.html', msg="该页面不存在！", state="404"), 404


@app.errorhandler(500)
def page_not_found(e):
    fun.pushMsg(title="服务器内部错误（HTTP状态码500）", content="{0}".format(e))
    return render_template('404.html', msg="服务器链接异常！", state="500"), 500


@app.route('/api/<path:filename>')
def download_file(filename):
    filename += ".json"
    return send_from_directory('saveFile/jsonFiles', filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

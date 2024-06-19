from flask import *
from flask_cors import *

from routes import Routes
from routes import adminRoutes

app = Flask(__name__)

app.config['DEBUG'] = False

CORS(app, supports_credentials=True)

# 注册路由
app.register_blueprint(Routes.routes_module)
app.register_blueprint(adminRoutes.routes_module)


# 自定义出错处理页面
@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template('404.html', msg="该页面不存在！", state="404"), 404


@app.errorhandler(500)
def page_not_found(e):
    print(e)
    return render_template('404.html', msg="服务器链接异常！", state="500"), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

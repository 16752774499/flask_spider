from flask import *
from flask_cors import *

from routes import Routes
from routes import adminRoutes

app = Flask(__name__)

app.config['DEBUG'] = True

CORS(app, supports_credentials=True)

# 注册路由
app.register_blueprint(Routes.routes_module)
app.register_blueprint(adminRoutes.routes_module)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

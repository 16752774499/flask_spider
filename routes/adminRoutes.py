from flask import render_template, Blueprint

# 创建蓝图对象
routes_module = Blueprint('adminRoutes', __name__)


@routes_module.route('/admin', methods=["GET"])
def admin():
    return render_template('AdminIndex.html')


@routes_module.route('/adminFrom', methods=["GET"])
def adminFrom():
    return render_template('AdminFrom.html')


@routes_module.route('/adminTask', methods=["GET"])
def adminTask():
    return render_template('AdminTask.html')


@routes_module.route('/adminTable', methods=["GET"])
def adminTable():
    return render_template('AdminlDtatTable.html')

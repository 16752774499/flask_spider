import json

from flask import render_template, Blueprint, request

# 创建蓝图对象
from script import fun

routes_module = Blueprint('adminRoutes', __name__)


@routes_module.route('/admin', methods=["GET"])
def admin():
    jobNums = fun.getJobsNums("all")
    classList = fun.getSearchKeywordClass()
    statusTrueNums = fun.viewStatus(True, "all")
    tasksList = fun.getTasksList()

    return render_template('AdminIndex.html', jobNums=jobNums, classNums=len(classList), statusTrueNums=statusTrueNums,
                           tasksList=tasksList, json=json)
    # json.loads()


@routes_module.route('/adminFrom', methods=["GET"])
def adminFrom():
    return render_template('AdminFrom.html')


@routes_module.route('/adminTask', methods=["GET"])
def adminTask():
    return render_template('AdminTask.html')


@routes_module.route('/adminTable', methods=["GET"])
def adminTable():
    return render_template('AdminlDtatTable.html')


@routes_module.route('/returnClassList', methods=["GET"])
def returnClassList():
    return json.dumps(fun.returnClassList())


@routes_module.route('/WeeklyDataVolumeList', methods=["GET"])
def WeeklyDataVolumeList():
    return json.dumps(fun.WeeklyDataVolumeList())


@routes_module.route('/checkTaskIdState', methods=["GET"])
def checkTaskIdState():
    taskId = request.args.get('taskId')
    redisSession = fun.returnRedisSession()
    taskIdState = redisSession.get(taskId)
    taskIdStateStraight = taskIdState.decode('utf-8')
    redisSession.close()
    print(taskIdStateStraight)
    return json.dumps({"state": str(taskIdStateStraight)})

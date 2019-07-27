from flask import request,jsonify
from flask import Blueprint


from model import *

user = Blueprint('user', __name__)


@user.route('/login/',methods = ['POST'])
def login():
    # 获取用户名和密码
    name = request.json.get("name")
    password = request.json.get("password")
    # 调用User类的查询方法
    user = User()
    one = user.queryObject(name,password)
    if(one!=None):
        result =  {"msg": "ok"}
    else:
        result = {"msg": "error"}
    return jsonify(result)


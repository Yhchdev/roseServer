from flask import request,jsonify
from flask import Blueprint


from model import *

rose = Blueprint('rose', __name__)


@rose.route('/table/',methods = ['GET'])
def getTableData():
    rose = Rose()
    objectSet = rose.queryRoseData()

    roseJsonArray = []
    for roseObj in objectSet:
        jsonStr = roseObj.to_json()
        roseJsonArray.append(jsonStr)

    return jsonify(object = roseJsonArray)

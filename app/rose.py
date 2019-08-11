from flask import jsonify
from flask import Blueprint
import time
from flask_csv import send_csv


from model import *

rose = Blueprint('rose', __name__)

CSVHead = ["id","total_max","total_mean","total_median","total_std","up_max","up_mean","up_median","up_std",
           "bottom_max","bottom_mean","bottom_median","bottom_std","height_max","height_mean","height_median","height_std",
            "grade","weight","create_time"]


# 返回表格里面的数据
@rose.route('/table/',methods = ['GET'])
def getTableData():
    rose = Rose()
    objectSet = rose.queryRoseData()

    roseJsonArray = []
    for roseObj in objectSet:
        roseDict = {"id":roseObj.id,"total_median":float(roseObj.total_median),"total_std":float(roseObj.total_std),
                    "up_median":float(roseObj.up_median),"up_std":float(roseObj.up_std),
                    "height_median":float(roseObj.height_median),"height_std":float(roseObj.height_std),
                    "bottom_median":float(roseObj.bottom_median),"bottom_std":float(roseObj.bottom_std),
                    "grade":roseObj.grade}
        roseJsonArray.append(roseDict)
    return jsonify(object = roseJsonArray)


# 返回csv文件
@rose.route("/csv/",methods = ['GET'])
def getCSV():
    rose = Rose()
    resultSet = rose.queryRoseData()
    roselist = []
    for roseIndex in resultSet:
        objDict = {"id":roseIndex.id, "total_max":roseIndex.total_max,"total_mean":roseIndex.total_mean,"total_median":roseIndex.total_median,"total_std":roseIndex.total_std,
                   "up_max":roseIndex.up_max, "up_mean":roseIndex.up_mean, "up_median":roseIndex.up_median,"up_std":roseIndex.up_std,
                   "bottom_max":roseIndex.bottom_max, "bottom_mean":roseIndex.bottom_mean, "bottom_median":roseIndex.bottom_median, "bottom_std":roseIndex.bottom_std,
                   "height_max": roseIndex.height_max, "height_mean":roseIndex.height_mean,"height_median":roseIndex.height_median,"height_std":roseIndex.height_std,
                   "grade":roseIndex.grade, 'weight':roseIndex.weight,'create_time':roseIndex.create_time}
        roselist.append(objDict)
    # 返回的csv默认名字

    timeVersion = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    csvName = 'roselist_{}.csv'.format(timeVersion)
    return send_csv(roselist,csvName, CSVHead)



# 返回均值 画图
@rose.route('/charts/mean/',methods = ['GET'])
def apiFormean():
    rose = Rose()
    resultSet = rose.queryRoseData()
    count_list = []
    count = 0
    total_max = 0
    total_median = 0
    total_mean = 0
    height_mean = 0
    stem_len = 0
    weight = 0
    for roseIndex in resultSet:
        count +=1
        total_max += roseIndex.total_max
        total_median  += roseIndex.total_median
        total_mean += roseIndex.total_mean
        height_mean += roseIndex.height_mean
        stem_len += roseIndex.stem_len
        weight += roseIndex.weight
    return [total_max/count,total_median/count,total_mean/count,height_mean/count,stem_len/count,weight/count]
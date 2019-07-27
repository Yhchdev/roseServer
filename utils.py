import json
import decimal


# 将decimal转为str (解决 == TypeError: Object of type 'Decimal' is not JSON serializable === 问题)
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)


# 将数据库里的记录下载为 CSV文件
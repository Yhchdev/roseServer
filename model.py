# coding: utf-8
import json
from sqlalchemy import *
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import create_session

from utils import DecimalEncoder

# 数据库连接配置
from configs import DB_URI

Base = declarative_base()

# 数据库引擎
engine = create_engine(DB_URI)
metadata = Base.metadata




# 创建事务
session = create_session(bind=engine)

# 部门表
class Department(Base):
    __tablename__ = 'department'

    id = Column(INTEGER(11), primary_key=True)
    department_name = Column(String(255))



# 雇员表
class Employee(Base):
    __tablename__ = 'employee'

    id = Column(INTEGER(11), primary_key=True)
    birth = Column(DateTime)
    email = Column(String(255))
    gender = Column(INTEGER(11))
    last_name = Column(VARCHAR(255))





# 玫瑰花属性数据
class Rose(Base):
    __tablename__ = 'rose'

    id = Column(INTEGER(255), primary_key=True)
    up_max = Column(Float(255, True))
    up_mean = Column(Float(255, True))
    up_median = Column(Float(255, True))
    up_std = Column(Float(255, True))
    bottom_max = Column(Float(255, True))
    bottom_mean = Column(Float(255, True))
    bottom_median = Column(Float(255, True))
    bottom_std = Column(Float(255, True))
    total_max = Column(Float(255, True))
    total_mean = Column(Float(255, True))
    total_median = Column(Float(255, True))
    total_std = Column(Float(255, True))
    height_max = Column(Float(255, True))
    height_mean = Column(Float(255, True))
    height_median = Column(Float(255, True))
    height_std = Column(Float(255, True))
    stem_len = Column(Float(255, True))
    weight = Column(Float(255, True))
    grade = Column(CHAR(255, 'utf8_bin'))
    create_time = Column(DateTime)

    def to_json(self):
        json_data = {
            'id': self.id,
            'bottom_max': self.bottom_max,
            'bottom_mean': self.bottom_mean,
            'bottom_median': self.bottom_median,
            'bottom_std': self.bottom_std,
            'create_time': self.create_time,
            'height_max': self.height_max,
            'height_mean': self.height_mean,
            'height_std': self.height_std,
            'total_max': self.total_max,
            'total_mean': self.total_mean,
            'total_median': self.total_median,
            'total_std': self.total_std,
            'up_max': self.up_max,
            'up_mean': self.up_mean,
            'up_median': self.up_median,
            'up_std': self.up_std,
            'grade': self.grade,
            'weight': self.weight,
            'stem_len':self.stem_len
        }
        return json.dumps(json_data,cls= DecimalEncoder)


    # 返回全部数据
    def queryRoseData(self):
        rose = session.query(Rose).all();
        return rose



# 用户表
class User(Base):
    __tablename__ = 'user'

    id = Column(INTEGER(11), primary_key=True)
    user_password = Column(String(255, 'utf8_bin'))
    user_name = Column(String(255, 'utf8_bin'))



    # 根据用户名和密码 查询单个对象
    def queryObject(self,userName,userPassword):
        user = session.query(User).filter(User.user_name == userName,User.user_password == userPassword).first()
        return user




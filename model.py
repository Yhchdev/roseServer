# coding: utf-8
from sqlalchemy import *
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import create_session

# 数据库连接配置
from configs import DB_URI

Base = declarative_base()

# 数据库引擎
engine = create_engine(DB_URI)
metadata = Base.metadata



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

    id = Column(INTEGER(11), primary_key=True)
    bottom_max = Column(Float(asdecimal=True))
    bottom_mean = Column(Float(asdecimal=True))
    bottom_median = Column(Float(asdecimal=True))
    bottom_std = Column(Float(asdecimal=True))
    create_time = Column(BIGINT(20))
    height_max = Column(Float(asdecimal=True))
    height_mean = Column(Float(asdecimal=True))
    height_median = Column(Float(asdecimal=True))
    height_std = Column(Float(asdecimal=True))
    total_max = Column(Float(asdecimal=True))
    total_mean = Column(Float(asdecimal=True))
    total_median = Column(Float(asdecimal=True))
    total_std = Column(Float(asdecimal=True))
    up_max = Column(Float(asdecimal=True))
    up_mean = Column(Float(asdecimal=True))
    up_median = Column(Float(asdecimal=True))
    up_std = Column(Float(asdecimal=True))
    grade = Column(CHAR(10))
    weight = Column(Float(asdecimal=True))





# 用户表
class User(Base):
    __tablename__ = 'user'

    id = Column(INTEGER(11), primary_key=True)
    user_password = Column(String(20))
    user_name = Column(String(50))

    # 查询单个对象
    def queryObject(self,userName,userPassword):
        user = session.query(User).filter(User.user_name == userName,User.user_password == userPassword).first()
        return user




# 创建事务
session = create_session(bind=engine)

# 测试数据库查询功能
rose = session.query(Rose).all()



#
# def show_query_result(rest):
#     for rose in rest:
#         print(rose.bottom_max)
#
# show_query_result(rest)
from sqlalchemy import *
from sqlalchemy.orm import create_session
from sqlalchemy.ext.declarative import declarative_base

from configs import DB_URI

Base = declarative_base()
engine = create_engine(DB_URI)
metadata = MetaData(bind=engine)

class Rose(Base):
    '''映射已有的数据库，传入三个参数：数据库名称、metadata（绑定接口）、autoload=True'''
    __table__ = Table('rose', metadata, autoload=True)

def show_query_result(rest):
    for rose in rest:
        print(rose.bottom_max)

# 创建事务
session = create_session(bind=engine)

# 测试数据库查询功能
rest = session.query(Rose).all()
show_query_result(rest)

print ('-' * 15)

# 测试增加记录功能
session.begin()
#session.add(School(name='Derek'))
session.commit()

# 查询增加结果
#rest = session.query(School).all()
show_query_result(rest)
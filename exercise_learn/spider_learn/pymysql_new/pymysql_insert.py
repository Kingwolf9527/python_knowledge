# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/27 0:24

import pymysql

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1',user='root',password='123456',database='python_test',charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cur
cur = db.cursor()

# SQL 插入语句
sql = """
    insert into company(id,emp_name) values(333,'kingwolf')
"""

try:
    #执行SQL语句
    cur.execute(sql)
    ## 提交到数据库执行，不是由游标来执行(记得一定要提交到数据库执行)
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()

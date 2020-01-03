# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/27 0:38

"""
    数据库查询操作
    Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。

    fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
    fetchall(): 接收全部的返回结果行.
    fetchmany(size): 可以获取指定条数的数据

"""

import pymysql

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1',user='root',password='123456',database='python_test',charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cur
cur = db.cursor()

#查询SQL语句
sql = """
select * from company ;

"""
#执行SQL
cur.execute(sql)
###################################fetchone()的用法###################################
# while True:
#     data = cur.fetchone()
#     if data:
#         print(data)
#     else:
#         break

# ###################################fetchall()的用法###################################
# results = cur.fetchall()
# for result in results:
#     print(result)

# ###################################fetchmany()的用法###################################
results = cur.fetchmany(2)
for result in results:
    print(result)


# 关闭数据库连接
db.close()


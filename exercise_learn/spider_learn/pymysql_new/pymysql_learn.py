# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/27 0:06

import pymysql

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1',user='root',password='123456',database='python_test',charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cur
cur = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cur.execute('show tables;')

# 使用 fetchone() 方法获取单条数据.
# data = cur.fetchall()
data = cur.fetchone()

print("tables include : %s" % data)

## 关闭数据库连接
db.close()
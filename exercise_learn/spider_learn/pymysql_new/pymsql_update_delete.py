# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/27 0:51

import pymysql

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1',user='root',password='123456',database='python_test',charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cur
cur = db.cursor()

# #SQL更新语句
# sql = """
# update company set emp_name = 'kingwolf' where id = 333;
#
# """


#SQL删除语句
sql = """
delete from company where id = 333;

"""

try:
    #执行语句
    cur.execute(sql)
    #把SQL语句提交给数据库执行
    db.commit()
except:
    #发生错误的时候，回滚
    db.rollback()


#关闭数据库连接
db.close()
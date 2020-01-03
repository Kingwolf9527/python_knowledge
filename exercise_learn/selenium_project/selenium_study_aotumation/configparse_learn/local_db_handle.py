# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/2/27 23:18

import pymysql
from selenium_study_aotumation.configparse_learn.read_config import Read_config

class Execute_sql(object):

    def __init__(self):
        self.data = Read_config()

    def con_db(self):
        '''连接数据库'''
        self.host = self.data.get_db('db_host')
        self.port = self.data.get_db('db_port')   #这里得到的port类型是str，需要把端口转为数字类型，才能连接数据库
        self.port = int(self.port)
        self.user = self.data.get_db('db_user')
        self.password = self.data.get_db('db_password')
        self.name = self.data.get_db('db_name')
        self.charset = self.data.get_db('db_charset')
        self.con = pymysql.connect(host=self.host,port=self.port,user=self.user,password=self.password,\
                                   database=self.name,charset=self.charset)
        self.cur = self.con.cursor()

    def operation_sql(self,sql,data):
        '''执行操作相关的数据SQL，例如：更新，删除，插入'''
        self.con_db()
        try:
            self.cur.execute(sql,data)
            self.con.commit()
        except Exception as e:
            print(e)
            self.con.rollback()
        finally:
            #调用关闭函数处理
            self.close_sql_con()

    def query_sql(self,sql):
        '''执行查询相关的数据SQL处理'''
        self.con_db()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def close_sql_con(self):
        '''关闭数据库连接'''
        self.cur.close()
        self.con.close()


if __name__ == '__main__':
    exe = Execute_sql()
    sql = 'select * from boss_zhipin'
    datas = exe.query_sql(sql)
    for data in datas:
        print(data)

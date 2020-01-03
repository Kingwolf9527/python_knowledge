# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/12/18 2:41

import pymysql
import os
import logging
from DBUtils.PersistentDB import PersistentDB
from DBUtils.PooledDB import PooledDB
from util.read_config import Read_Config

class Db_utils_processing(object):

    def __init__(self,is_mult_thread):

        filename_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'config')
        filename = os.path.join(filename_dir, "db.ini")

        #读取db配置信息
        self.host = Read_Config(filename).get_value('Database_config','host')
        self.user = Read_Config(filename).get_value('Database_config','user')
        self.password = Read_Config(filename).get_value('Database_config','password')
        #端口需要转为整形
        self.port = int(Read_Config(filename).get_value('Database_config','port'))
        self.db_name = Read_Config(filename).get_value('Database_config','db_name')
        self.charset = Read_Config(filename).get_value('Database_config','charset')

        #判断是否采用多线程
        if is_mult_thread:
            #指定数据库连接驱动以及最大连接数,设置阻塞等待，以及相关配置信息
            self.pooldb = PooledDB(creator=pymysql,maxconnections=5,blocking=True,host=self.host,\
                              user=self.user,password=self.password,port=self.port,\
                              database=self.db_name,charset=self.charset)
        else:
            # 指定数据库连接驱动以及连接最大复用次数
            self.pooldb = PersistentDB(creator=pymysql,maxusage=1000,host=self.host,\
                              user=self.user,password=self.password,port=self.port,\
                              database=self.db_name,charset=self.charset)

        #建立连接以及创建游标
        self.db = self.pooldb.connection()
        self.cur = self.db.cursor()

    def select_Db(self,sql):

        """
        负责查询语句
        :param sql:
        :return:
        """
        try:
            self.cur.execute(sql)
            results = self.cur.fetchall()   #打印数据，这里可以自由处理(返回的数据是一个元祖)
            print(len(results))
            for result in results:
                print(result)
        except:
            logging.info('------ Error: unable to fecth data       ------')
            logging.error('------ {sql} :   {}      ------').format(sql)
        finally:
            self.close_db()

    def insert_Db(self, sql):

        """
        负责插入数据语句
        :param sql:
        :return:
        """
        try:
            effect_row = self.cur.execute(sql)
            # 涉及数据变化，需要connection对象的commit操作
            self.db.commit()
            return effect_row
        except:
            logging.error('------ {sql} :   {}      ------').format(sql)
            # 数据操作错误，回滚事务
            self.db.rollback()
        finally:
            self.close_db()

    def update_Db(self, sql):

        """
        负责更新数据语句
        :param sql:
        :return:
        """
        try:
            effect_row = self.cur.execute(sql)
            # 涉及数据变化，需要connection对象的commit操作
            self.db.commit()
            return effect_row
        except:
            logging.error('------ {sql} :   {}      ------').format(sql)
            # 数据操作错误，回滚事务
            self.db.rollback()
        finally:
            self.close_db()

    def delete_Db(self, sql):

        """
        负责删除数据语句
        :param sql:
        :return:
        """
        try:
            effect_row = self.cur.execute(sql)
            # 涉及数据变化，需要connection对象的commit操作
            self.db.commit()
            return effect_row
        except:
            logging.error('------ {sql} :   {}      ------').format(sql)
            # 数据操作错误，回滚事务
            self.db.rollback()
        finally:
            self.close_db()

    def close_db(self):
        """
        关闭数据库连接
        :return:
        """
        self.cur.close()
        self.db.close()



if __name__ == '__main__':

    sql = 'select * from xici;'
    t = Db_utils_processing(is_mult_thread=True)
    t.select_Db(sql)




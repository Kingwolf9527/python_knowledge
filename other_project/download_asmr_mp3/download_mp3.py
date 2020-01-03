# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/1/10 0:02

from urllib import request
from db_config import DB_config as df
import pymysql
import os

class Download_mp3(object):


    def connect_mysql(self):

        #配置数据库连接
        db_parms = {
            'host' : df['host'],
            'port' : df['port'],
            'user' : df['user'],
            'password' : df['password'],
            'database' : df['db'],
            'charset' : df['charset']
        }

        #连接数据库
        self.con = pymysql.connect(**db_parms)

        #设置游标
        self.cur = self.con.cursor()

        #传con和cur给查询函数
        self.select_sql_cur(self.con,self.cur)

    def select_sql_cur(self,con,cur):

        #查询SQL
        select_sql = """
            SELECT article_title,mp3_url FROM asmr WHERE mp3_url <> '暂无数据';
        """
        try:
            #执行SQL
            self.cur.execute(select_sql)
            #任意获取数据
            datas = self.cur.fetchall()
            if datas:
                for data in datas:
                    name = data[0]
                    #完整的文件名
                    name = name + '.mp3'
                    mp3_url = data[1]
                    print(mp3_url)
                    self.download(name,mp3_url)
        except pymysql.Error as e:
            print('Error is:',e)
            #回滚
            con.rollback()
        finally:
            #关闭游标
            cur.close()
            #关闭连接
            con.close()

    def download(self,name,mp3_url):

        #mp3目录保存路径
        dir_path = os.path.join(os.path.dirname(__file__),'asmr_mp3')
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        #mp3文件保存路径
        file_path = os.path.join(dir_path,name)

        #下载mp3
        request.urlretrieve(mp3_url,file_path)


if __name__ == '__main__':
    download = Download_mp3()
    download.connect_mysql()


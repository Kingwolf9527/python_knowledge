# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from pymysql import cursors
from mysql_config.db_config import DB_config as df
from twisted.enterprise import adbapi   #数据库异步处理数据

class JianshuPipeline(object):

    def __init__(self):
        self._sql = None

    def process_item(self, item, spider):

        # 设置数据库的连接文件
        db_params = {
            'host': df['host'],
            'port': df['port'],
            'user': df['user'],
            'password': df['password'],
            'database': df['db'],
            'charset': df['charset']
        }
        # 连接数据库
        self.connect = pymysql.connect(**db_params)
        # 创建游标
        self.cur = self.connect.cursor()

        #插入数据，并处理
        try:
            self.cur.execute(self.old_insert_sql,(item['title'],item['author'],item['avatar'],item['pub_time'],item['content'],item['origin_url'],item['article_id'],item['word_count'],item['read_count'],item['comment_count'],item['like_count'],item['subjects']))
            #提交到数据库服务器
            self.connect.commit()
        except pymysql.Error as e:
            print(e)
            #发生错误，回滚数据
            self.connect.rollback()
        #关闭数据库连接
        self.connect.close()
        return item

    @property
    def old_insert_sql(self):
        if not self._sql:
            self._sql = """
                insert into article(title,author,avatar,pub_time,content,origin_url,article_id,word_count,read_count,comment_count,like_count,subjects) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            return self._sql
        return self._sql



class Jianshu_TwistedPipeline(object):

    def __init__(self):
        self._sql = None

    @property
    def insert_sql(self):
        if not self._sql:
            self._sql = """
                insert into article(title,author,avatar,pub_time,content,origin_url,article_id,word_count,read_count,comment_count,like_count,subjects) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            return self._sql
        return self._sql

    def process_item(self,item,spider):

        # 设置数据库的连接文件
        db_params = {
            'host': df['host'],
            'port': df['port'],
            'user': df['user'],
            'password': df['password'],
            'database': df['db'],
            'charset': df['charset'],
            'cursorclass' : cursors.DictCursor         #游标的处理
        }

        # 数据库连接池
        self.dbpool = adbapi.ConnectionPool('pymysql',**db_params)

        #处理数据
        deal_with_data = self.dbpool.runInteraction(self.insert_item,item)   #第一个参数是可以调用的对象，就是一个函数，对传入的参数做处理
        #异常处理
        deal_with_data.addErrback(self.handle_error,item,spider)   #传入item和spider，可以清晰知道哪个item或者spider出现问题

    def insert_item(self,cursor,item):
        #插入数据
        cursor.execute(self.insert_sql,(item['title'],
                                        item['author'],
                                        item['avatar'],
                                        item['pub_time'],
                                        item['content'],
                                        item['origin_url'],
                                        item['article_id'],
                                        item['word_count'],
                                        item['read_count'],
                                        item['comment_count'],
                                        item['like_count'],
                                        item['subjects']
                                        )
                       )


    def handle_error(self,error,item,spider):
        #处理异常信息的函数
        print('='*50)
        print(error)
        print('=' * 50)


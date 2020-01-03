# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymysql import cursors
from twisted.enterprise import adbapi
from db_config import DB_config as df

class AsmrPipeline(object):

    def __init__(self):

        #配置数据库
        db_parms = {
            'host' : df['host'],
            'port' : df['port'],
            'user' : df['user'],
            'password' : df['password'],
            'database' : df['db'],
            'charset' : df['charset'],
            'cursorclass' : cursors.DictCursor
        }
        #配置数据库连接池
        self.dbpool = adbapi.ConnectionPool('pymysql',**db_parms)


    def process_item(self, item, spider):

        #处理数据
        deal_with_data = self.dbpool.runInteraction(self.insert_item,item)
        #处理异常
        deal_with_data.addErrback(self.handle_error,item,spider)
        return item


    def insert_item(self,cursor,item):

        #插入语句
        insert_sql = """
            insert into asmr(article_title,update_time,category,pic_url,video_url,mp3_url) values(%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(insert_sql,(item['article_title'],item['update_time'],item['category'],str(item['pic_url']),item['video_url'],item['mp3_url']))


    def handle_error(self,error,item,spider):
        print('='*50)
        print('Error is ：%s' %error)
        print('='*50)

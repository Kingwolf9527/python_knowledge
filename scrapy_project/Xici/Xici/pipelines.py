# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from pymysql import cursors
from db_config import DB_config as df
from twisted.enterprise import adbapi

class XiciPipeline(object):

    def __init__(self):
        db_parms = {
            'host' : df['host'],
            'port' : df['port'],
            'user' : df['user'],
            'password' : df['password'],
            'database' : df['db'],
            'charset' : df['charset'],
            'cursorclass': cursors.DictCursor               #twisted的异步存储数据，用到pymysql的游标
        }
        #连接数据库连接池
        self.dbpool = adbapi.ConnectionPool('pymysql',**db_parms)
        
        
    def process_item(self, item, spider):

        #处理数据
        deal_with_data = self.dbpool.runInteraction(self.insert_item,item)
        #处理异常
        deal_with_data.addErrback(self.handle_error,item,spider)
        return item


    def insert_item(self,cursor,item):

        insert_sql = """
                insert into xici(ip_address,port,server_address,anonymity,type,speed,connect_time,survive_time,verify_time)  values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(insert_sql,(item['ip_address'],item['port'],item['server_address'],item['anonymity'],item['type'],item['speed'],item['connect_time'],item['survive_time'],item['verify_time']))


    def handle_error(self,error,item,spider):
        print('='*50)
        print('Error is：%s' % error)
        print('='*50)
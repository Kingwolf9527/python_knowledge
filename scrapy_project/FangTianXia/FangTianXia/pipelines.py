# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
"""

    第一种方式：用json数据保存

"""
# from scrapy.exporters import JsonLinesItemExporter
# from FangTianXia.items import NewhouseItem,EsfhouseItem,ZuhouseItem
#
# class HousePipeline(object):
#
#     def __init__(self):
#         #创建保存数据的json文件，包括新房文件
#         self.newhouse_fp = open('newhouse.json','wb')
#         self.esfhouse_fp = open('esfhouse.json', 'wb')
#         self.zuhouse_fp = open('zuhouse.json', 'wb')
#
#         #创建导出对象
#         self.exporter_newhouse = JsonLinesItemExporter(self.newhouse_fp,ensure_ascii=False,encoding='utf-8')
#         self.exporter_esfhouse = JsonLinesItemExporter(self.esfhouse_fp, ensure_ascii=False,encoding='utf-8')
#         self.exporter_zuhouse = JsonLinesItemExporter(self.zuhouse_fp, ensure_ascii=False,encoding='utf-8')
#
#     def open_spider(self,spider):
#         print('。。。爬虫开始了。。。')
#
#
#     def process_item(self, item, spider):
#
#         #处理数据,需要判断属于哪个item的，因为有多个item
#         if isinstance(item,NewhouseItem):
#             self.exporter_newhouse.export_item(item)
#         elif isinstance(item,EsfhouseItem):
#             self.exporter_esfhouse.export_item(item)
#         elif isinstance(item,ZuhouseItem):
#             self.exporter_zuhouse.export_item(item)
#
#         return item
#
#
#     def close_spider(self,spider):
#         #关闭文件
#         self.newhouse_fp.close()
#         self.esfhouse_fp.close()
#         self.zuhouse_fp.close()
#         print('。。。爬虫结束了。。。')


"""

    第二种方式：存在mysql数据库中

"""
import pymysql
from pymysql import cursors
from db_config import DB_config as df
from twisted.enterprise import adbapi
from FangTianXia.items import NewhouseItem,EsfhouseItem,ZuhouseItem


class House_mysqlPipeline(object):

    def __init__(self):

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
        self.db_pool = adbapi.ConnectionPool('pymysql',**db_params)


    def process_item(self,item,spider):

        if isinstance(item,NewhouseItem):
            # 处理数据
            deal_with_data = self.db_pool.runInteraction(self.newhouse_insert_item,item)  #第一个参数是可以调用的对象，就是一个函数，对传入的参数做处理
            # 异常处理
            deal_with_data.addErrback(self.handle_error,item,spider)   #传入item和spider，可以清晰知道哪个item或者spider出现问题

        elif isinstance(item,EsfhouseItem):
            # 处理数据
            deal_with_data = self.db_pool.runInteraction(self.esfhouse_insert_item,item)  # 第一个参数是可以调用的对象，就是一个函数，对传入的参数做处理
            # 异常处理
            deal_with_data.addErrback(self.handle_error, item, spider)  # 传入item和spider，可以清晰知道哪个item或者spider出现问题

        elif isinstance(item,ZuhouseItem):
            # 处理数据
            deal_with_data = self.db_pool.runInteraction(self.zuhouse_insert_item,item)  # 第一个参数是可以调用的对象，就是一个函数，对传入的参数做处理
            # 异常处理
            deal_with_data.addErrback(self.handle_error, item, spider)  # 传入item和spider，可以清晰知道哪个item或者spider出现问题
        return item

    def newhouse_insert_item(self,cursor,item):
        # 插入新房数据
        if isinstance(item,NewhouseItem):

            newhouse_sql = """
                                insert into newhouse(province,city,name,rooms,area,address,district,price,sale,type,origin_url) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """
            cursor.execute(newhouse_sql,(item['province'],item['city'],item['name'],item['rooms'],item['area'],item['address'],item['district'],item['price'],item['sale'],item['type'],item['origin_url']))

    def esfhouse_insert_item(self, cursor, item):
        # 插入二手房数据
        if isinstance(item, EsfhouseItem):

            esfhouse_sql = """
                                insert into esfhouse(province,city,name,rooms,area,floor,towards,build_year,address,price,unit_price,origin_url) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """
            cursor.execute(esfhouse_sql, (item['province'], item['city'], item['name'], item['rooms'], item['area'], item['floor'],item['towards'], item['build_year'], item['address'], item['price'], item['unit_price'], item['origin_url']))

    def zuhouse_insert_item(self, cursor, item):
        # 插入租房数据
        if isinstance(item, ZuhouseItem):

            zuhouse_sql = """
                                insert into zuhouse(province,city,district,street,name,rent,rooms,area,towards,unit_price,subway,advantage,origin_url) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """
            cursor.execute(zuhouse_sql, (item['province'], item['city'], item['district'], item['street'], item['name'], item['rent'],item['rooms'], item['area'], item['towards'], item['unit_price'], item['subway'],item['advantage'], item['origin_url']))


    def handle_error(self,error,item,spider):
        # 通用的处理异常信息的函数
        print('='*50)
        print('Rrror is：',error)
        print('=' * 50)
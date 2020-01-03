# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter
import pymysql
from mysql_config.db_config import DB_config as df

class BossJobPipeline(object):

    def open_spider(self,spider):
        self.fp = open('position.json','wb')
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
        print('。。。爬虫开始了。。。')

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.fp.close()
        print('。。。爬虫结束了。。。')


#数据保存到mysql数据库中
class Boss_mysql(object):

    def process_item(self,item,spider):

        #连接数据库
        self.connet = pymysql.connect(host=df['host'], port=df['port'], user=df['user'], passwd=df['password'],
                                      database=df['db'], charset=df['charset'])
        #创建游标
        self.cur = self.connet.cursor()

        # 使用 execute()  方法执行 SQL 插入数据
        sql = """
                insert into boss_zhipin(company_name,position_name,salary,city,work_year,education,positon_descs,advantage,introduce,work_address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)

             """
        company_name = item['company_name']
        position_name = item['position_name']
        salary = item['salary']
        city = item['city']
        work_year = item['work_year']
        education = item['education']
        positon_descs = item['positon_descs']
        advantage = item['advantage']
        introduce = item['introduce']
        work_address = item['work_address']

        try:
            # 执行SQL插入语句
            self.cur.execute(sql, (str(company_name),
                                    str(position_name),
                                    str(salary),
                                    str(city),
                                    str(work_year),
                                    str(education),
                                    str(positon_descs),
                                    str(advantage),  # 因为我设计的表结构都是varchar类型，所以，所以数据都是字符串才能保存到数据库，因为advantage字段获取到的每一个元素都是list，存不进数据库，需要转为str处理
                                    str(introduce),
                                    str(work_address)
                                )
                        )
            # 提交到数据库执行
            self.connet.commit()
        except pymysql.Error as e:
            print(e)
            # 如果发生错误则回滚
            self.connet.rollback()
        # 关闭连接
        self.connet.close()
        return item
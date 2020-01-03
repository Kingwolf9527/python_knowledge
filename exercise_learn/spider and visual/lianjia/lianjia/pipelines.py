# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

# 数据库配置信息
db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'python_test',
    'charset': 'utf8'
}


class LianjiaPipeline(object):

    # 获取数据库连接和游标
    def __init__(self):
        self.connection = pymysql.connect(**db_config)     #**kwargs :可以连接多个参数，需要是字典  *args ：需要是元祖touple
        self.cur = self.connection.cursor()

    # Pipeline必须实现的方法，对收集好的item进行一系列处理
    def process_item(self, item, spider):
        # 存储的SQL语句
        sql = "insert into lianjia_chengjiao(region, href, name, style, area, orientation,decoration,elevator,floor,build_year,sign_time,unit_price,total_price,fangchan_class,subway) values(%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        try:
            self.cur.execute(sql,(item['region'].encode("utf-8"),
                                  item['href'].encode("utf-8"),
                                  item['name'].encode("utf-8"),
                                  item['style'].encode("utf-8"),
                                  item['area'].encode("utf-8"),
                                  item['orientation'].encode("utf-8"),
                                  item['decoration'].encode("utf-8"),
                                  item['elevator'].encode("utf-8"),
                                  item['floor'].encode("utf-8"),
                                  item['build_year'].encode("utf-8"),
                                  item['sign_time'],
                                  item['unit_price'],
                                  item['total_price'],
                                  item['fangchan_class'],
                                  item['subway']
                                    )
                             )
            #提交数据
            self.connection.commit()
        except pymysql.Error as e:
            # 若存在异常则抛出
            print(e.args)

        return item
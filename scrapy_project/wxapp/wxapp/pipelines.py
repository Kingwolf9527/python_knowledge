# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


#数据量较大，用json存储
from scrapy.exporters import JsonLinesItemExporter

class WxappPipeline(object):

    def __init__(self):
        #爬虫开始之前，先打开文件(没有就创建文件)
        self.fp = open('wxapp_test2.json','wb')

        #创建导出文件
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')

    def open_spider(self,spider):
        print('爬虫开始了。。。')

    def process_item(self, item, spider):
        #处理json数据
        self.exporter.export_item(item)
        return item    #因为pipeline有可能有多个，前面的处理完了item，如果不把item返回去，其他的pipeline获取不到item了，就无法处理item数据了

    def close_spider(self,spider):
        print('爬虫结束了。。。')
        #爬虫结束，关闭文件
        self.fp.close()
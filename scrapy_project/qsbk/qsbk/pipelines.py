# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#
# import json
#
# class QsbkPipeline(object):
#
#     def __init__(self):
#         #爬虫开始前，打开文件(没有就创建文件)
#         self.fp = open('duanzi2.json','w',encoding='utf-8')
#
#     #爬虫开始函数
#     def open_spider(self,spider):
#         print('段子的爬虫开始了......')
#
#     #爬虫处理数据的函数，item数据是爬虫文件通过yield传过来的数据
#     def process_item(self, item, spider):
#
#         #因为要把json数据写进文件中，但是item文件是一个字典，需要先转化为json数据，在写进文件(注意：在json.dumps()方法中，这个ensure_ascii=False，要设置成这样，才能把转化后的数据保存为中文)
#         # item_json = json.dumps(item,ensure_ascii=False)
#         item_json = json.dumps(dict(item),ensure_ascii=False)   #因为采用items文件处理需要保存的字段，因此，这个时候获取的item不是一个字典，是一个类的处理方法，所以不能直接被json转为字典，需要先把它转为字典
#         #写入文件
#         self.fp.write(item_json +'\n')
#         return item
#
#     #爬虫的关闭函数
#     def close_spider(self,spider):
#         #爬虫结束后，关闭文件
#         self.fp.close()
#         print('段子爬虫结束了......')

#
# """
#
#     运行scrapy内置的导出json数据的JsonItemExporter类来处理，后面就不需要再处理item数据了,
#
# """
#
# from scrapy.exporters import JsonItemExporter
#
# class QsbkPipeline(object):
#
#     def __init__(self):
#
#         #爬虫开始前，打开文件(没有就创建文件),注意：JsonItemExporter类处理数据都是通过二进制bytes类型的，因此，文件的写入方式也需要是bytes类型
#         self.fp = open('duanzi.json','wb')     #以二进制的方式打开文件，不能知道编码格式
#         #创建一个导入文件类
#         self.exporter = JsonItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
#         #开始处理数据
#         self.exporter.start_exporting()
#
#     #爬虫开始函数
#     def open_spider(self,spider):
#         print('段子的爬虫开始了......')
#
#     #爬虫处理数据的函数，item数据是爬虫文件通过yield传过来的数据
#     def process_item(self, item, spider):
#
#         #直接接收数据来处理
#         self.exporter.export_item(item)
#         return item
#
#     #爬虫的关闭函数
#     def close_spider(self,spider):
#
#         # 结束导出json处理
#         self.exporter.finish_exporting()    #JsonItemExporter方法的一个缺陷，就是它一直把数据存储在内存里，等到finish_exporting()方法执行完了，再把所有数据写入一个列表中，如果数据很大，就会有问题，耗内存
#
#         #爬虫结束后，关闭文件
#         self.fp.close()
#         print('段子爬虫结束了......')


"""

    针对JsonItemExporter缺陷的改良方法，JsonLinesItemExporter()方法，推荐使用这个方法

"""

from scrapy.exporters import JsonLinesItemExporter

class QsbkPipeline(object):

    def __init__(self):

        #爬虫开始前，打开文件(没有就创建文件),注意：JsonItemExporter类处理数据都是通过二进制bytes类型的，因此，文件的写入方式也需要是bytes类型
        self.fp = open('duanzi_new3.json','wb')     #以二进制的方式打开文件，不能知道编码格式
        #创建一个导入文件类
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')

    #爬虫开始函数
    def open_spider(self,spider):
        print('段子的爬虫开始了......')

    #爬虫处理数据的函数，item数据是爬虫文件通过yield传过来的数据
    def process_item(self, item, spider):

        #直接接收数据来处理
        self.exporter.export_item(item)
        return item

    #爬虫的关闭函数
    def close_spider(self,spider):

        #爬虫结束后，关闭文件
        self.fp.close()
        print('段子爬虫结束了......')
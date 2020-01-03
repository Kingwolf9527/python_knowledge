# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os

class BiquyunPipeline(object):

    def open_spider(self,spider):
        print('。。。爬虫开始。。。')

    def process_item(self, item, spider):

        #判断是否存在笔趣阁的文件夹，没有就创建
        novel_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),u'笔趣阁')
        if not os.path.exists(novel_file_path):
            os.mkdir(novel_file_path)
        novel = '{}.txt'.format(item['novel_name'])
        novel_path = os.path.join(novel_file_path,novel)
        with open(novel_path,'a+',encoding='utf-8') as fp:
            fp.write(item['chapter_name'] + '\n' + item['chapter_content'])

        return item


    def close_spider(self,spider):
        print('。。。爬虫结束了。。。')
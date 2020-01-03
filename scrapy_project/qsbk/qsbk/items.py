# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QsbkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #作者
    author = scrapy.Field()
    #段子的内容
    content_duanzi = scrapy.Field()
    #段子的被人觉得好笑的数据
    smile_data = scrapy.Field()
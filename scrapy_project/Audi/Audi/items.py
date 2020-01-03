# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AudiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #图片分类
    category = scrapy.Field()

    #图片url
    image_urls = scrapy.Field()

    #images，image_urls都是ImagesPipeline所需要的参数
    images = scrapy.Field()


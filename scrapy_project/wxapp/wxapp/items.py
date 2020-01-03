# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WxappItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 推荐文章的标题
    title = scrapy.Field()
    # 文章的作者
    author = scrapy.Field()
    # 文章的发表时间
    pub_time = scrapy.Field()
    # 文章的内容
    article_content = scrapy.Field()
    # 被阅读的次数
    GitHub_Star = scrapy.Field()

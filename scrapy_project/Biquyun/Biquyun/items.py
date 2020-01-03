# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BiquyunItem(scrapy.Item):

    # 小说名称
    novel_name = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 最后更新的时间
    last_update_time = scrapy.Field()
    # 头像
    avatar = scrapy.Field()
    # 小说的主要内容介绍
    novel_intro = scrapy.Field()
    # 章节名字
    chapter_name = scrapy.Field()
    #每一章节的内容
    chapter_content = scrapy.Field()
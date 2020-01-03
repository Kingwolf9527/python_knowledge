# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AsmrItem(scrapy.Item):

    # 文章的标题
    article_title = scrapy.Field()
    # 最后的更新时间
    update_time = scrapy.Field()
    # 分类
    category = scrapy.Field()
    # 图片url
    pic_url = scrapy.Field()
    # 视频的url
    video_url = scrapy.Field()
    # 如果视频是以mp3格式,mp3_url
    mp3_url = scrapy.Field()

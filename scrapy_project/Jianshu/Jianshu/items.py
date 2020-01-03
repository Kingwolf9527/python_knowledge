# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuItem(scrapy.Item):

    # 文章的标题
    title = scrapy.Field()
    # 文章作者
    author = scrapy.Field()
    # 头像
    avatar = scrapy.Field()
    # 发布时间
    pub_time = scrapy.Field()
    # 文章所有内容，包括样式
    content = scrapy.Field()
    # 文章的url
    origin_url = scrapy.Field()
    # 文章的id
    article_id = scrapy.Field()
    #文章字数
    word_count = scrapy.Field()
    #文章阅读数
    read_count = scrapy.Field()
    #文章的评论数
    comment_count = scrapy.Field()
    #文章喜欢数
    like_count = scrapy.Field()
    #文章所属的专题
    subjects = scrapy.Field()

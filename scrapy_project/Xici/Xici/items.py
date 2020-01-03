# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiciItem(scrapy.Item):

    #IP地址
    ip_address = scrapy.Field()
    #端口
    port = scrapy.Field()
    #服务器地址
    server_address = scrapy.Field()
    #是否匿名
    anonymity = scrapy.Field()
    #类型
    type = scrapy.Field()
    #速度
    speed = scrapy.Field()
    #连接时间
    connect_time = scrapy.Field()
    #存活时间
    survive_time = scrapy.Field()
    #验证时间
    verify_time = scrapy.Field()
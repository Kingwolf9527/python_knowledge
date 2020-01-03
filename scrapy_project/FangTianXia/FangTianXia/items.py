# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewhouseItem(scrapy.Item):
    #省份
    province = scrapy.Field()
    #城市
    city = scrapy.Field()
    # 楼盘名字
    name = scrapy.Field()
    # 几居的房源
    rooms = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 行政区
    district = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 是否在售或者预售
    sale = scrapy.Field()
    # 房源的类型
    type = scrapy.Field()
    # 房源详情页面的url
    origin_url = scrapy.Field()


class EsfhouseItem(scrapy.Item):
    # 省份
    province = scrapy.Field()
    # 城市
    city = scrapy.Field()
    #小区名字
    name = scrapy.Field()
    #几居几室
    rooms = scrapy.Field()
    #建造面积
    area = scrapy.Field()
    #楼层，层高
    floor = scrapy.Field()
    #朝向
    towards = scrapy.Field()
    #建造时间
    build_year = scrapy.Field()
    #地址
    address = scrapy.Field()
    #总价
    price = scrapy.Field()
    #均价
    unit_price = scrapy.Field()
    #详情页面的url
    origin_url = scrapy.Field()


class ZuhouseItem(scrapy.Item):
    # 省份
    province = scrapy.Field()
    # 城市
    city = scrapy.Field()
    #行政区
    district = scrapy.Field()
    #街道
    street = scrapy.Field()
    #小区名字
    name = scrapy.Field()
    #是否整租
    rent = scrapy.Field()
    #几室几厅
    rooms = scrapy.Field()
    #建造面积
    area = scrapy.Field()
    #朝向
    towards = scrapy.Field()
    #单价
    unit_price = scrapy.Field()
    #地铁线路距离
    subway = scrapy.Field()
    #房源优势所在
    advantage = scrapy.Field()
    #房源的详情页面url
    origin_url = scrapy.Field()

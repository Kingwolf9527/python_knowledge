# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BossJobItem(scrapy.Item):

    # 职位名称
    position_name = scrapy.Field()
    # 薪水
    salary = scrapy.Field()
    # 工作城市
    city = scrapy.Field()
    # 工作年限
    work_year = scrapy.Field()
    # 学历
    education = scrapy.Field()
    # 公司名称
    company_name = scrapy.Field()
    # 职位描述
    positon_descs = scrapy.Field()
    # 公司优势
    advantage = scrapy.Field()
    # 公司介绍
    introduce = scrapy.Field()
    # 工作地址
    work_address = scrapy.Field()
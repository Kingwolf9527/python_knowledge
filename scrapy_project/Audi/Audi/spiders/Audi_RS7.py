# -*- coding: utf-8 -*-
import scrapy
from Audi.items import AudiItem

class AudiRs7Spider(scrapy.Spider):
    name = 'Audi_RS7'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/2994.html']

    def parse(self, response):
        #获取所有分类，就是例如：车身外观，中控方向盘之类的
        uiboxs = response.xpath('//div[@class="column grid-16"]/div[@class="uibox"]')[1:]     #因为第一个uibox是全景看车，不需要获取
        for uibox in uiboxs:

            #获取分类,后续把属于这个分类的图片，下载到相应的分类中
            category = uibox.xpath('.//div[@class="uibox-title"]/a/text()').get()

            #获取图片的url
            urls = uibox.xpath('.//ul/li/a/img/@src').getall()
            #把url补充完整，获取到url都是有点缺失的，缺少了头部的"https:",可以用到scrapy自带的一个方法urljoin()自动补全url(这个方法有个前提，必须是同一个域下的)，再结合map函数，把所有获取到的url都补全
            urls = list(map(lambda url:response.urljoin(url),urls))          #map对象需要转为list

            #创建一个字典来存储数据
            item = AudiItem()
            item['category'] = category
            item['image_urls'] = urls

            yield item
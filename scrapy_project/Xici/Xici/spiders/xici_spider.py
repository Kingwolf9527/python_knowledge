# -*- coding: utf-8 -*-
import scrapy
from Xici.items import XiciItem
import re

class XiciSpiderSpider(scrapy.Spider):
    name = 'xici_spider'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/nn/1']

    def parse(self, response):

        #创建一个字典来存储数据
        item = XiciItem()

        #获取所有行数据的tr标签,因为第一个tr标签是描述的，不需要，从第二个开始取，做一个切片
        trs = response.xpath('//table[@id="ip_list"]//tr')[1:]
        for tr in trs:

            #IP地址
            ip_address = tr.xpath('./td[2]/text()').get()
            item['ip_address'] = ip_address

            #端口
            port = tr.xpath('./td[3]/text()').get()
            item['port'] = port

            #服务器地址
            server_address = tr.xpath('./td[4]//text()').getall()
            if server_address:
                server_address = ''.join(server_address).strip()
                item['server_address'] = server_address
            else:
                item['server_address'] = '暂无数据'

            #是否匿名
            anonymity = tr.xpath('./td[5]/text()').get()
            item['anonymity'] = anonymity

            #类型
            type = tr.xpath('./td[6]/text()').get()
            item['type'] = type

            # 速度
            speed = tr.xpath('./td[7]/div/@title').get()
            item['speed'] = speed

            ##连接时间
            connect_time = tr.xpath('./td[8]/div/@title').get()
            item['connect_time'] = connect_time

            # 存活时间
            survive_time = tr.xpath('./td[9]/text()').get()
            item['survive_time'] = survive_time

            # 验证时间
            verify_time = tr.xpath('./td[last()]/text()').get()
            item['verify_time'] = verify_time

            yield item

        #下一页的url
        next_url = response.xpath('//div[@class="pagination"]/a[contains(@class,"next_page")]/@href').get()
        next_url = response.urljoin(next_url)
        if next_url:
            #最后一页没有url返回
            yield scrapy.Request(url=next_url,callback=self.parse)


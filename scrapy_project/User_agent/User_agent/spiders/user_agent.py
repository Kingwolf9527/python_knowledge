# -*- coding: utf-8 -*-
import scrapy
import json

class UserAgentSpider(scrapy.Spider):
    name = 'user_agent'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/user-agent']

    def parse(self, response):
        #json字符串转为字典
        u_agent = json.loads(response.text)['user-agent']
        print('='*50)
        print(u_agent)
        yield scrapy.Request(self.start_urls[0],dont_filter=True)
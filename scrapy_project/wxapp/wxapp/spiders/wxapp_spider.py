# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

#处理导入模块文件的问题，可以快速导进不同文件
import sys
sys.path.append('wxapp/')

#把items模板文件导进来
from wxapp.items import WxappItem


class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']


    rules = (
        #LinkExtractor(allow=(是需要满足正则表达式的条件))
        Rule(LinkExtractor(allow=r'.+?mod=list&catid=2&page=\d'),follow=True), #这里不需要用到callback回调函数来解析，只需要获取文章详情页的url
        Rule(LinkExtractor(allow=r'.+/article-.+\.html'),callback='parse_detail',follow=False), #这个规则是为了提取所有满足条件的详情页url来解析，follow=False为了防止冲突
    )


    def parse_detail(self, response):

        #文章的标题
        title = response.xpath('//h1[@class="ph"]/text()').get()

        author_a = response.xpath('//p[@class="authors"]')
        # 文章的作者
        author = author_a.xpath('./a/text()').get()

        #文章的发表时间
        pub_time = author_a.xpath('./span/text()').get()

        #文章的内容
        article_content = response.xpath('//td[@id="article_content"]//text()').getall()
        #转为字符串
        article_content = ''.join(article_content).strip()

        #被阅读的次数
        GitHub_Star = response.xpath('//div[@class="cl"]/div/a/text()').get()

        #实例化一个字典来存储数据
        item = WxappItem()

        item['title'] = title
        item['author'] = author
        item['pub_time'] = pub_time
        item['article_content'] = article_content
        item['GitHub_Star'] = GitHub_Star

        yield item
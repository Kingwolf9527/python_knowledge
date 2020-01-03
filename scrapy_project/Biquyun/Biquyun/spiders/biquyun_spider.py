# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Biquyun.items import BiquyunItem


class BiquyunSpiderSpider(CrawlSpider):
    name = 'biquyun'
    allowed_domains = ['biquyun.com']
    start_urls = ['http://www.biquyun.com']

    rules = (
        #获取小说详情页面
        Rule(LinkExtractor(allow=r'.*/\d+_\d+/'), callback='parse_novel', follow=True),
    )

    def parse_novel(self, response):

        #小说名称
        novel_name = response.xpath('//div[@id="info"]/h1/text()').get()

        #作者
        author = response.xpath('//div[@id="info"]/p[1]/text()').get()
        # author = author.replace(u'作    者：','')

        #最后更新的时间
        last_update_time = response.xpath('//div[@id="info"]/p[3]/text()').get()
        # last_update_time = last_update_time.replace(u'最后更新：','')

        #头像
        avatar = response.xpath('//div[@id="fmimg"]/img/@src').get()

        #小说的主要内容介绍
        novel_intro = response.xpath('//div[@id="intro"]/p/text()').get()
        # novel_intro = novel_intro.strip()

        #创建一个字典来存储数据
        item = BiquyunItem()
        item['novel_name'] = novel_name
        item['author'] = author
        item['last_update_time'] = last_update_time
        item['avatar'] = avatar
        item['novel_intro'] = novel_intro


        #章节对应的url
        chapter_urls = response.xpath('//div[@id="list"]/dl/dd/a/@href').getall()
        chapter_urls =list(map(lambda url:response.urljoin(url),chapter_urls))   #补充完整的章节url
        for chapter_url in chapter_urls:
            # 再次请求所有章节的url
            request = scrapy.Request(chapter_url, callback=self.parse_chapter, meta={'item': item})  # 把这个item数据共享


            return request


    def parse_chapter(self,response):

        #共享item
        item = response.meta['item']

        #每一章节的名字
        chapter_name = response.xpath('//div[@class="bookname"]/h1/text()').get()

        #每一章节的内容
        chapter_content = response.xpath('//div[@id="content"]//text()').getall()
        chapter_content = ''.join(chapter_content)

        item['chapter_name'] = chapter_name
        item['chapter_content'] = chapter_content

        yield item
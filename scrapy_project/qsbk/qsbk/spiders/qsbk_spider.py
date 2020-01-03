# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem                  #要把需要保存的数据字段从items模板文件中，导进爬虫文件中

class QsbkSpiderSpider(scrapy.Spider):
    #爬虫的名字必须唯一,爬虫项目中，允许有多个爬虫
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    domain_url = 'https://www.qiushibaike.com'

    def parse(self, response):

        #获取所有的div标签，每一个div标签，代表一个段子
        duanzi_divs = response.xpath('//div[@id="content-left"]/div')
        for duanzi_div in duanzi_divs:

            #获取作者,运用extract_first()方法去获取第一条数据，或者用get()方法，一样的效果，最后通过strip()方法，去掉前后的空格
            #get = extract_first ，返回的是列表的第一条数据//  getall = extract ,返回的是一个列表
            author = duanzi_div.xpath('.//div[@class="author clearfix"]//h2/text()').extract_first().strip()

            #获取段子的内容
            content_duanzi = duanzi_div.xpath('.//div[@class="content"]/span/text()').extract()
            content_duanzi = ''.join(content_duanzi).strip()

            #获取段子的被人觉得好笑的数据
            smile_data = duanzi_div.xpath('.//div[@class="stats"]/span/i/text()').extract_first().strip()


            #设置一个字典用于存储数据
            item = {}
            #作者
            item['author'] = author
            #段子的内容
            item['content_duanzi'] =content_duanzi
            #赞的数量
            item['smile_data'] = smile_data


            yield item

            #分页数据爬取的处理
            next_url = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').extract_first()

            #这里需要判断，如果已经是最后一页，最后一个li标签就不是下一页的了，直接返回，不用处理数据
            if not next_url:
                return
            else:
                #scrapy再次请求的方法是scrapy.Request(url(下一页的url),callback=(回调的方法)),注意：完整的下一页url
                yield scrapy.Request(self.domain_url+next_url,callback=self.parse)




            # duanzi = {
            #
            #     'author' : author,
            #     'content_duanzi': content_duanzi,
            #     'smile_data': smile_data
            #
            # }
            #把循环变为生成器，一个一个数据的提交
            # yield duanzi

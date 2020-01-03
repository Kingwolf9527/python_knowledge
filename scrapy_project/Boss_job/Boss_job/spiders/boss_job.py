# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Boss_job.items import BossJobItem


class BossJobSpider(CrawlSpider):
    name = 'boss_job'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c100010000/?query=%E5%AE%89%E5%85%A8%E6%B8%97%E9%80%8F&page=1']

    rules = (
        #匹配分页，获取所有职位页面的规则
        Rule(LinkExtractor(allow=r'.+?query=%E5%AE%89%E5%85%A8%E6%B8%97%E9%80%8F&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'.+job_detail/.+\.html'),callback='parse_job',follow=False)
    )

    def parse_job(self, response):

        #职位名称
        position_name = response.xpath('//div[@class="name"]/h1/text()').get()

        #薪水
        salary = response.xpath('//div[@class="name"]/span/text()').get().strip()

        #相关城市，教育信息
        info = response.xpath('//div[@class="job-primary detail-box"]/div[@class="info-primary"]/p/text()').getall()
        #工作城市
        city = info[0].replace(r'城市：','')

        #工作年限
        work_year = info[1].replace(r'经验：','')

        #学历
        education = info[2].replace(r'学历：','')

        #公司名称
        company_name = response.xpath('//div[@class="info-company"]/h3/a/text()').get()

        #职位描述
        positon_descs = response.xpath('//div[@class="job-sec"]/div[@class="text"]//text()').getall()
        positon_descs = ''.join(positon_descs).strip()

        #公司优势
        advantage = response.xpath('//div[@class="job-sec"]/div[@class="job-tags"]/span/text()').getall()

        # 公司介绍
        introduce = response.xpath('//div[@class="job-sec company-info"]/div[@class="text"]/text()').getall()
        introduce = ''.join(introduce).strip()

        # 工作地址
        work_address = response.xpath('//div[@class="location-address"]/text()').get()

        #设置一个字典存储数据
        item = BossJobItem()
        item['position_name'] = position_name
        item['salary'] = salary
        item['city'] = city
        item['work_year'] = work_year
        item['education'] = education
        item['company_name'] = company_name
        item['positon_descs'] = positon_descs
        item['advantage'] = advantage
        item['introduce'] = introduce
        item['work_address'] = work_address

        yield item
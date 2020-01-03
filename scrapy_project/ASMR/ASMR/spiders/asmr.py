# -*- coding: utf-8 -*-
import scrapy
import re
from ASMR.items import AsmrItem

class AsmrSpider(scrapy.Spider):
    name = 'asmr'
    allowed_domains = ['asmrv.com']
    start_urls = ['https://www.asmrv.com/page/1']

    def parse(self, response):

        #获取所有文章的url
        article_urls = response.xpath('//div[contains(@class,"excerpts")]/article/a/@href').getall()
        for article_url in article_urls:
            #传给解析函数处理
            yield scrapy.Request(url=article_url,callback=self.parse_article)

        #下一页url
        next_url = response.xpath('//li[contains(@class,"next-page")]/a/@href').get()
        if next_url:
            yield scrapy.Request(url=next_url,callback=self.parse)


    def parse_article(self,response):

        #创建一个字典存储数据
        item = AsmrItem()

        #文章的标题
        article_title = response.xpath('//div[@class="container"]/h1/text()').get()
        item['article_title'] = article_title

        #最后的更新时间
        update_time = response.xpath('//div[@class="focusbox-text"]/span/text()').get()
        update_time = re.sub(r'更新时间 : ','',update_time)
        item['update_time'] = update_time

        #分类
        category = response.xpath('//div[contains(@class,"article-tags")]/a/text()').getall()
        category = '/'.join(category).strip()
        item['category'] = category

        #图片url列表,也有两种图片的url处理
        pic_url = response.xpath('//li/img/@src | //img[@class="alignnone size-full"]/@src').getall()
        if pic_url:
            item['pic_url'] = pic_url
        else:
            item['pic_url'] = '暂无数据'

        #视频的url
        video_url = response.xpath('//article[@class="article-content"]/iframe/@src').get()
        #获取到url是:https://www.asmrv.com/panurl.php?url=https://pan.asmrv.com/Kkyuu/SP6njkkow.mp4，需要切割处理，https://pan.asmrv.com/Kkyuu/SP6njkkow.mp4，这个才是目标url,而且不是每个视频都有的，有些是mp3，需要另外处理
        if video_url:
            url_split = video_url.split('=')
            video_url = url_split[1]
            item['video_url'] = video_url
        else:
            item['video_url'] = '暂无数据'

        #如果视频是以mp3格式，用这个保存
        mp3_url = response.xpath('//div[@class="wp-player"]/@data-address').get()
        if mp3_url:
            #、获取到url也需要处理：https://pan.asmrv.com/luna/4sdanjo.mp3|，需要去掉后面的|
            mp3_url = mp3_url.split('|')[0]
            item['mp3_url'] = mp3_url
        else:
            item['mp3_url'] = '暂无数据'

        yield item


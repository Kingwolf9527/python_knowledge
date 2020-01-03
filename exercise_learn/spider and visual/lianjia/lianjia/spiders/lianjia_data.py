# -*- coding: utf-8 -*-
import scrapy
import re
import json
from lxml import html
from urllib.parse import quote
from lianjia.items import LianjiaItem





'''
    思路：
    以行政区为单位，先获取广州地区所有的小区信息(因为正常的通过翻页，最多只能获取到（30*100）3000条数据，但是如果从行政区变为小区，小区下面有具体的房源，就能获取尽可能多得数据了)
    以小区为单位，获取每一个小区里面的房源数据
    最后就是获取具体的每一个房源的信息。
    
'''
class LianjiaDataSpider(scrapy.Spider):
    name = 'lianjia_chengjiao'
    allowed_domains = ['gz.lianjia.com']

    regions = {
        'tianhe':'天河',
        'yuexiu':'越秀',
        'liwan':'荔湾',
        'haizhu': '海珠',
        'panyu': '番禺',
        'baiyun': '白云',
        'haungpugz': '黄埔',
        'conghua': '从化',
        'zengcheng': '增城',
        'huadou': '花都',
        'nansha': '南沙'
    }
    # start_urls = ['http://gz.lianjia.com/chengjiao/']
    def start_requests(self):
        #以行政区为单位，目的是爬取每一个行政区的小区列表
        for region in list(self.regions.keys()):
            url = "https://gz.lianjia.com/xiaoqu/" + region + "/"
            yield scrapy.Request(url=url,callback=self.parse,meta={'region':region})   #用来获取页码

    def parse(self, response):
        region = response.meta['region']
        selector = html.etree.HTML(response.text)
        #获取每个行政区的具体小区的数据，就是总共有几页，获取页码，例如：{"totalPage":30,"curPage":1}，这里的小区是总的小区数据
        sel = selector.xpath('//div[@class="page-box house-lst-page-box"]/@page-data')[0]  #这里取的是"totalPage"-总页码
        sel = json.loads(sel)  #转为字典
        total_pages = sel['totalPage']
        #然后遍历一下页码，页码需要转化为int类型
        for i in  range(int(total_pages)):
            # 需要格式化一下，把行政区域添加进去，又因为i是从0开始的，而且url里面是字符串，所以i也需要转化为字符串类型,用str()转
            url_page = "https://gz.lianjia.com/xiaoqu/{}/pg{}/".format(region,str(i+1))
            yield scrapy.Request(url=url_page,callback=self.parse_xiaoqu,meta={'region':region})

    def parse_xiaoqu(self,response):
        #上面返回了每一个页面的信息，这个时候我们就把当前页面的小区列表拿到，而后，在针对小区列表，每一个小区进行一次请求
        selector = html.etree.HTML(response.text)
        #获取具体每页的小区名字
        xiao_list = selector.xpath('//div[@class="title"]/a/text()')
        for xq_name in xiao_list:
            #根据不同的小区名称，查找成交的数据，例如：https://gz.lianjia.com/chengjiao/rs美林湖畔花园/
            url_xq = "https://gz.lianjia.com/chengjiao/rs" + quote(xq_name) + "/"
            yield  scrapy.Request(url=url_xq,callback=self.parse_chengjiao,meta={'region':response.meta['region'],'xq_name':xq_name})

    def parse_chengjiao(self,response):
        xq_name = response.meta['xq_name']
        #解析小区的页面数，上面说到了，我们请求了每一个小区数据，这个小区肯定不止包含一页的数据，那么我们这个方法就是将这个小区包含的页面数抽取出来，而后针对每一个页面进行请求
        selector = html.etree.HTML(response.text)
        content = selector.xpath('//div[@class="page-box house-lst-page-box"]')   #页码有可能为空，就是只有一页的情况
        total_pages = 0
        #针对这种场景，增加一个判断
        if len(content):
            page_data = json.loads(content[0].xpath('./@page-data')[0])
            # 获取总的页面数量
            total_pages = page_data['totalPage']

        for i in range(int(total_pages)):
            #需要格式化一下，把页码（url是字符串，所以需要转化）添加进去，以及小区的名称，例如：https://gz.lianjia.com/chengjiao/pg2rss骏景花园/
            xq_chengjiao_url = "https://gz.lianjia.com/chengjiao/pg{}rs{}/".format(str(i+1),quote(xq_name))
            yield scrapy.Request(url=xq_chengjiao_url,callback=self.parse_content,meta={'region':response.meta['region']})


        #解析具体的页面了，可以看到，这个方法里面包含了非常多的条件判断，这是因为，我们之前定义的item字段里面的信息，并不是每一个小区都有的，就是说，我们要的信息他不是一个规规矩矩的信息，很多的房源没有提供相关的信息，比如地铁，周边学校等等的信息，我们这里就是如果有这个信息，我们就把它提取出来，如果没有的话，我们就给他自定义一个内容。最后将item提交给item pipeline进行后续的处理
    def parse_content(self,response):
        selector = html.etree.HTML(response.text)
        #整个成交页面的显示信息
        chengjiao_list = selector.xpath('//ul[@class="listContent"]/li')
        #进行遍历所有页面，对所有的items加判断，因为有部分item，不是所有小区都有的
        for cj in chengjiao_list:
            #进行实例化
            item = LianjiaItem()
            item['region'] = self.regions.get(response.meta['region'])

            #房源的链接
            href = cj.xpath('./a/@href')
            if not len(href):
                continue
            item['href'] = href[0]

            #获取房源名称，房源结构，小区
            data_content = cj.xpath('.//div[@class="title"]/a/text()')
            if len(data_content):
                # 按照空格分割成一个列表,例如这样的数据：骏景花园 4室2厅 143.53平米
                data_content = data_content[0].split()
                item['name'] = data_content[0]
                item['style'] = data_content[1]
                item['area'] = data_content[2]

            #获取朝向,装修,电梯,例如这样的数据：北 | 精装 | 有电梯
            data_content= cj.xpath('.//div[@class="houseInfo"]/text()')
            if len(data_content):
                data_content = data_content[0].split('|')
                item['orientation'] = data_content[0]
                item['decoration'] = data_content[1]
                #因为有一些小区是没有电梯，这里需要加一个判断
                if len(data_content) == 3:  #因为如果是有电梯的，上面的分割，是有三个元素的，因此判断长度是不是等于3，就可以得知是否有电梯
                    item['elevator'] = data_content[2]
                else:
                    item['elevator'] = '无'

            #获取楼层高度，建造时间,例如这样的数据：中楼层(共13层) 2003年建塔楼
            data_content = cj.xpath('.//div[@class="positionInfo"]/text()')
            if len(data_content):
                data_content = data_content[0].split()
                item['floor'] = data_content[0]
                #因为有可能没有建造的时间，是那些很旧的小区，这种场景
                if len(data_content) == 2:
                    item['build_year'] = data_content[1]
                else:
                    item['build_year'] = '无'

            #获取签约时间
            data_content = cj.xpath('.//div[@class="dealDate"]/text()')
            if len(data_content):
                item['sign_time'] = data_content[0]

            #获取总价
                data_content = cj.xpath('.//div[@class="totalPrice"]/span/text()')
            if len(data_content):
                item['total_price'] = data_content[0]

            #获取每平米单价
                data_content = cj.xpath('.//div[@class="unitPrice"]/span/text()')
            if len(data_content):
                item['unit_price'] = data_content[0]

            #获取房产类型，周边学校，周边地铁，例如这样的数据：房屋满五年 距4号线车陂南958米（但是，不是所有小区都有地铁或者学校，或者房屋满几年的，都是需要判断的）
            # data_content = cj.xpath('.//span[@class="dealHouseTxt"]/span/text()')
            #获取房产类型
            #/span[contains(text(),"房屋满")]/text() :是提取当前span标签下包含"房屋满"的文本(contains(text(),*kw))，模糊匹配，后面要加上/text() ，否则会翻译不了匹配到的文字
            data_content = cj.xpath('.//span[@class="dealHouseTxt"]/span[contains(text(),"房屋满")]/text()')
            if len(data_content):
                item['fangchan_class'] = data_content[0]
            else:
                item['fangchan_class'] = '无'

            #获取周边地铁
            data_content = cj.xpath('.//span[@class="dealHouseTxt"]/span[contains(text(),"号线")]/text()')
            if len(data_content):
                item['subway'] = data_content[0]
            else:
                item['subway'] = '无'

            yield item



            #
            # if len(str_data_content):
            #     for i in data_content:
            #         if i.find("房屋满") != -1:  # 找到了返回的是非-1的数，找不到的返回的是-1
            #             item['fangchan_class'] = i
            #         elif i.find("号线") != -1:
            #             item['subway'] = i
            #         elif i.find("学") != -1:
            #             item['school'] = i
            # yield item

















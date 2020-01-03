# -*- coding: utf-8 -*-
import scrapy
import re
from FangTianXia.items import NewhouseItem,EsfhouseItem,ZuhouseItem

class FangtianxiaSpider(scrapy.Spider):
    name = 'fangtianxia'
    allowed_domains = ['fang.com']
    start_urls = ['https://www.fang.com/SoufunFamily.htm']

    def parse(self, response):
        #获取所有城市的tr标签
        trs = response.xpath('//div[@class="outCont"]//tr')
        #初始省份文本为none
        province = None

        for tr in trs:
            #获取第二个和第三个td标签，第一个td标签有class属性，去掉
            tds = tr.xpath('.//td[not(@class)]')
            #省份
            province_td = tds[0]
            #提取省份文本
            province_text = province_td.xpath('.//text()').get()
            #如果是省份城市有多行，第二行起，那个td标签的文本没有，只有空格的转义(&nbsp;)，需要处理一下
            province_text = re.sub(r'\s','',province_text)
            #需要判断一下，因为如果该省份有多个城市，城市列表有多行，就需要继承前面获取到的省份了，非第一行的城市列表是没有省份td标签的
            if province_text:
                province = province_text

            #不爬取海外的房源，就是省份为“其它”的
            if province == '其它':
                continue

            #城市
            city_td = tds[1]
            city_links = city_td.xpath('.//a')
            for city_link in city_links:
                city = city_link.xpath('.//text()').get()
                city_url = city_link.xpath('.//@href').get()
                #构造新房的url
                url_moudle = city_url.split('//')
                str_url = url_moudle[0]   #例如：http:
                domain = url_moudle[1]
                domain_str = domain.split('.')
                #城市的简写
                domain_code = domain_str[0] #例如：bj,sh

                #这里要处理一下特殊情况，就是北京市，它的新房，二手房，租房的url规律跟其他城市都不同
                # 北京新房的url：https://newhouse.fang.com/house/s/
                # 北京二手房的url：https://esf.fang.com/
                # 北京的租房url：https://zu.fang.com/
                if 'bj' in domain_code:
                    #北京新房url
                    newhouse_url = 'https://newhouse.fang.com/house/s'
                    #北京二手房的url
                    esf_url = 'https://esf.fang.com'
                    #北京租房的url
                    zu_url = 'https://zu.fang.com'

                else:
                    #最终构造出的新房url
                    newhouse_url = str_url + '//' + domain_code + '.newhouse.fang.com/house/s'

                    #构造二手房的url
                    esf_url = str_url + '//' + domain_code + '.esf.fang.com'

                    #构造租房的url
                    zu_url = str_url + '//' + domain_code + '.zu.fang.com'

                #构造新房的请求，解析新房的页面数据,同时需要共享省份和城市的数据，用meta方法
                yield scrapy.Request(url=newhouse_url,callback=self.parse_newhouse,meta={'info':(province,city)})

                #构造二手房的请求，解析二手房的页面数据,同时需要共享省份和城市的数据，用meta方法
                yield scrapy.Request(url=esf_url,callback=self.parse_esf,meta={'info':(province,city)})

                # 构造租房的请求，解析租房的页面数据,同时需要共享省份和城市的数据，用meta方法
                yield scrapy.Request(url=zu_url, callback=self.parse_zu, meta={'info': (province, city)})

            #     break    #这两个break是调试使用的
            # break

    def parse_newhouse(self,response):

        #获取共享的省份城市数据
        province,city = response.meta.get('info')

        #获取所有楼盘的房源
        lis = response.xpath('//div[contains(@class,"nl_con")]/ul/li')
        for li in lis:

            #楼盘名字
            name = li.xpath('.//div[@class="nlcd_name"]/a/text()').get()
            if name:
                name = name.strip()
            else:
                name = '暂无数据'

            #几居的房源,是一个列表，可能是1局，可能是2居，3居等等
            house_type_list = li.xpath('.//div[contains(@class,"house_type")]/a/text()').getall()
            if house_type_list:
                house_type_list = list(map(lambda x:re.sub(r'\s','',x),house_type_list))
                rooms = list(filter(lambda x:x.endswith('居'),house_type_list))        #因为有少数的楼盘没有写多少居，写其他的，需要过滤这些数据
                rooms = '/'.join(rooms).strip()
            else:
                rooms = '暂无数据'

            #面积
            area = li.xpath('.//div[contains(@class,"house_type")]/text()').getall()
            if area:
                area = ''.join(area).strip()
                area = re.sub(r'\s|/|－','',area)
            else:
                area = '暂无数据'

            #地址,如果直接获取文本，会发现不全，因为，在文本中用...代替过长的地址
            address = li.xpath('.//div[contains(@class,"address")]/a/@title').get()

            #行政区,例子：[白云区],提取中括号里面的文本信息，用正则的search方法查询，最后通过group()提取
            district_list = li.xpath('.//div[contains(@class,"address")]/a//text()').getall()
            district_text = ''.join(district_list).strip()
            if district_text:
                district = re.search(r'.*\[(.+)\].*',district_text).group(1)
            else:
                district = '暂无数据'

            #价格，需要全部提取文本，因为有部分是多少钱一套的，大部分是均价（注意，尽量还是用getall方法，防止提取不全）
            price = li.xpath('.//div[@class="nhouse_price"]//text()').getall()
            price = ''.join(price).strip()
            price = price.replace(r'广告|\s','')

            #是否在售或者预售
            sale = li.xpath('.//div[contains(@class,"fangyuan")]/span/text()').get()

            #房源的类型，例如：普遍住宅等等
            type = li.xpath('.//div[contains(@class,"fangyuan")]/a/text()').getall()
            type = '/'.join(type).strip()

            # 房源详情页面的url
            origin_url = li.xpath('.//div[@class="nlcd_name"]/a/@href').get()
            if origin_url:
                origin_url = 'https:' + origin_url
            else:
                origin_url = '暂无数据'

            #创建一个字典来存储数据
            item = NewhouseItem()
            item['name'] = name
            item['rooms'] = rooms
            item['area'] = area
            item['address'] = address
            item['district'] = district
            item['price'] = price
            item['sale'] = sale
            item['type'] = type
            item['origin_url'] = origin_url
            item['province'] = province
            item['city'] = city

            yield item

        #获取下一页的链接,这个提取不在for循环里面
        next_url = response.xpath('//div[@class="page"]/ul/li/a[@class="next"]/@href').get()
        if next_url:
            #防止获取的下一页不完整，采用response.urljoin()方法可以补充完整，循环调用的解析函数还是本身，meta数据也需要继续共享；如果没有下一页，就不需要
            yield scrapy.Request(url=response.urljoin(next_url),callback=self.parse_newhouse,meta={'info': (province, city)})

    def parse_esf(self,response):

        # 获取共享的省份城市数据
        province, city = response.meta.get('info')

        #获取所有房源的dl标签
        dls = response.xpath('//div[contains(@class,"shop_list")]/dl')
        for dl in dls:
            #创建字典存储数据
            item = EsfhouseItem()

            # 小区名字
            name = dl.xpath('.//p[@class="add_shop"]/a/@title').get()
            item['name'] = name

            #几居几室，楼层等信息
            infos = dl.xpath('.//p[@class="tel_shop"]/text()').getall()
            for info in infos:
                if '厅' in info:
                    item['rooms'] =info.strip()

                elif '㎡' in info:
                    item['area'] = info.strip()

                elif '层' in info:
                    item['floor'] = info.strip()

                elif '向' in info:
                    item['towards'] = info.strip()

                elif '年' in info:
                    build_year = info.strip()
                    build_year = re.sub(r'建|\s','',build_year)
                    item['build_year'] = build_year


            #地址
            address = dl.xpath('.//p[@class="add_shop"]/span/text()').get()
            item['address'] = address

            # 总价
            price = dl.xpath('.//dd[@class="price_right"]/span[@class="red"]//text()').getall()
            price = ''.join(price).strip()
            item['price'] = price

            #均价
            unit_price = dl.xpath('.//dd[@class="price_right"]/span[2]/text()').get()
            item['unit_price'] = unit_price

            # 详情页面的url
            origin_url = dl.xpath('.//dd/h4/a/@href').get()
            #url不完整，需要补充完整
            origin_url = response.urljoin(origin_url)
            item['origin_url'] = origin_url

            #省份，城市
            item['province'] = province
            item['city'] = city

            yield item

        #获取下一页
        next_url = response.xpath('//div[@class="page_al"]/p[last()-2]/a/@href').get()
        next_url = response.urljoin(next_url)
        #前面99页都是相同的效果，就是最后一页特殊，需要其他处理,最后一页的倒数第三个p标签是首页的url，首页的url是没有i3的,其他页面都有的
        if '/house/i3' in next_url:
            yield scrapy.Request(url=next_url,callback=self.parse_esf,meta={'info': (province, city)})




    def parse_zu(self,response):

        # 获取共享的省份城市数据
        province, city = response.meta.get('info')

        #创建字典存储数据
        item = ZuhouseItem()

        #获取所有房源的dl标签
        dls = response.xpath('//div[contains(@class,"houseList")]/dl')
        for dl in dls:
            #行政区，街道，小区等等信息
            infos = dl.xpath('.//p[@class="gray6 mt12"]/a/span/text()').getall()
            if infos:
                # 行政区
                district = infos[0]
                item['district'] = district
                #街道
                street = infos[1]
                item['street'] = street
                ##小区名字,但是小区名字可能没有，只有行政区和街道，这里需要加多判断，因为这里的infos列表基本固定是三个元素，只有特殊情况才只有两个
                if len(infos) == 3:
                    name = infos[2]
                    item['name'] = name
                else:
                    item['name'] = '暂无数据'

            #整租，几室几厅等等信息
            descs = dl.xpath('.//p[@class="font15 mt12 bold"]/text()').getall()
            for desc in descs:
                if '租' in desc:
                    #是否整租，也有可能合租
                    rent = desc.strip()
                    item['rent'] = rent
                elif '厅' in desc:
                    #几室几厅，可能是多少户人合租
                    rooms = desc.strip()
                    item['rooms'] = rooms
                elif '㎡' in desc:
                    #建造面积
                    area = desc.strip()
                    item['area'] = area
                elif '朝' in desc:
                    # 朝向,有些房源是没有朝向的,如果列表有四个元素，就说明有朝向
                    towards = desc
                    towards = towards.strip()
                    item['towards'] = towards
                else:
                    item['towards'] = '暂无数据'


            ##单价
            unit_price = dl.xpath('.//p[@class="mt5 alingC"]//text()').getall()
            if unit_price:
                unit_price = ''.join(unit_price).strip()
                item['unit_price'] = unit_price
            else:
                item['unit_price'] = '暂无数据'

            # 地铁线路距离,这里需要加判断，很多城市没有地铁的
            subway = dl.xpath('.//p[@class="mt12"]/span[@class="note subInfor"]/text()').getall()
            if subway:
                subway = ''.join(subway).strip()
                item['subway'] = subway
            else:
                item['subway'] = '暂无开通的地铁线路'

            #房源优势所在
            advantage = dl.xpath('.//p[@class="mt12"]/span[contains(@class,"note color")]/text()').getall()
            if advantage:
                advantage = '/'.join(advantage).strip()
                item['advantage'] = advantage
            else:
                item['advantage'] = '暂无数据'

            # 房源的详情页面url
            origin_url = dl.xpath('.//p[@class="title"]/a/@href').get()
            origin_url = response.urljoin(origin_url)
            item['origin_url'] = origin_url

            #省份，城市
            item['province'] = province
            item['city'] = city

            yield item

        #下一页的链接url
        next_url = response.xpath('//div[@class="fanye"]/a[last()-1]/@href').get()
        next_url = response.urljoin(next_url)
        #这里做一个判断，如果是最后一页了，倒数第二个a获取的url跟response.url不一致，就一直执行函数，如果是一致，意味着是最后一页了，不用再执行
        if response.url != next_url:
            yield scrapy.Request(url=next_url,callback=self.parse_zu,meta={'info': (province, city)})

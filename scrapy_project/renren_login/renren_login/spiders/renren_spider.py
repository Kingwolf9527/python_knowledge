# -*- coding: utf-8 -*-
import scrapy


class RenrenSpiderSpider(scrapy.Spider):
    name = 'renren_spider'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    """
    
        因为是要发送post请求，就需要重写start_requests()方法了，因为这个方法是默认采用get方式，遍历start_urls里面的所有url，采用scrapy.FormRequest(url=,formdata=,callback=)方法
    
    """

    def start_requests(self):

        #登陆的url
        url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=20181132018543'

        #登陆的数据
        data = {
            'email' : '13726229967',
            'password' : '922521dfxs',
            'icode': '' ,
            'origURL': 'http://www.renren.com/home',
            'domain' : 'renren.com',
            'key_id': '1',
            'captcha_type': 'web_login',
            'rkey': '95ca078b85bf95cb0514c548f8e2efec',
            'f': 'https://www.baidu.com'
        }


        request = scrapy.FormRequest(url,formdata=data,callback=self.parse_page)
        yield request

    #这个函数主要是为了验证登陆是否成功的，如果登录成功，就访问大鹏的主页url
    def parse_page(self, response):

        #大鹏主页的url
        url = 'http://www.renren.com/880151247/profile'
        request_profile = scrapy.Request(url,callback=self.parse_profile)

        yield request_profile

    #最后通过返回大鹏主页的HTML页面来验证登陆是否成功
    def parse_profile(self, response):

        with open('renren.html','w',encoding='utf-8') as fp:
            fp.write(response.text)



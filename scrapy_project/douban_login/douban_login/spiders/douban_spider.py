# -*- coding: utf-8 -*-
import scrapy
from urllib import request
from PIL import Image
from aip import AipOcr

class DoubanSpiderSpider(scrapy.Spider):

    name = 'douban_spider'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/login']

    # 登录url
    login_url = 'https://accounts.douban.com/login'
    # 个人中心的url
    profile_url = 'https://www.douban.com/people/kingwolf9527/'
    # 修改个人签名的url
    signature_url = 'https://www.douban.com/j/people/kingwolf9527/edit_signature'

    def parse(self, response):

        fromdata = {

            'source' : 'None',
            'redir': 'https://douban.com/',
            'form_email': 'lccr777@163.com',
            'form_password': '922521dfxs',
            'remember' : 'on',
            'login' : '登录'
        }

        #其他两个动态变化的关于验证码的参数，另外通过其他方式获取
        captcha_url = response.xpath('//img[@id="captcha_image"]/@src').get()
        if captcha_url:       #因为有可能会没有获取到验证码，正常登录是没有验证码出现的，所以需要增加一个判断
            #获取到验证码
            captcha = self.recognize_captcha(captcha_url)
            fromdata['captcha-solution'] = captcha   #captcha-solution的值就是输入的验证码
            #获取captcha_id，有验证码出现。才会出现这个元素定位
            captcha_id = response.xpath('//input[@name="captcha-id"]/@value').get()
            fromdata['captcha-id'] = captcha_id
        #在发送完整的post请求去登陆
        yield scrapy.FormRequest(self.login_url,formdata=fromdata,callback=self.parse_recongnize_login)

    def parse_recongnize_login(self,response):

        # #正常登录成功后，会自动调整到豆瓣首页，登录失败，还会在登录页面
        # if response.url == 'https://www.douban.com/':
        #或者通过比较登录页面后，昵称是否一致就可以判断登录是否成功了
        nickname = response.xpath('//li[@class="nav-user-account"]//span/text()').get()
        if nickname == 'kingwolf的帐号':
            #在发送一个请求，进入个人中心，后续修改签名
            yield scrapy.Request(self.profile_url,callback=self.parse_profile)
            print('登录成功！')
        else:
            print('登录失败！')

    def parse_profile(self,response):

        print(response.url)
        if response.url == self.profile_url:
            print('恭喜，进入个人中心！')
            #修改个人签名
            ck = response.xpath('//form[@name="edit_sign"]//input[@name="ck"]/@value').get()
            #因为修改签名，需要发送一个post请求
            form_data = {
                'ck' : ck,
                'signature' : 'kingwolf！'
            }
            #回调函数不需要了，但是不加上callback会默认调用scrapy自带的parse方法，所以需要指定一个none的回调函数
            yield scrapy.FormRequest(url=self.signature_url,formdata=form_data,callback=self.parse_none)       #在scrapy中，如果scrapy.FormRequest()方法中，如果不指定callback函数，它就会默认执行scrapy默认的的parse()方法；；解决的方法是：把callback指定一个空函数
        else:
            print('很遗憾，没有进入个人中心！')

    def parse_none(self,response):
        pass

    def recognize_captcha(self,captcha_url):

        # #把验证码下载下来手动输入识别
        # request.urlretrieve(captcha_url,'captcha.jpg')
        # #然后打开下载下来的验证码图片
        # image = Image.open('captcha.jpg')
        # #把验证码展示出来
        # image.show()
        # #输入验证码
        # captcha = input("请输入验证码：")
        # return captcha

        # 配置AipOcr,利用百度的api自动识别验证码
        APP_ID = '11223350'
        API_Key = 'K0QoGISeULWbNNr3sYYNDchA'
        Secret_Key = '5kLp3QYL8rMEUh6ooiLGjXhrXW1ZxUF2'

        client = AipOcr(APP_ID, API_Key, Secret_Key)

        # 把验证码下载下来
        request.urlretrieve(captcha_url, 'captcha.jpg')

        # 读取图片
        def get_file_content(filepath):
            with open(filepath, 'rb') as fp:
                return fp.read()

        image = get_file_content(r'captcha.jpg')

        # 有可选参数
        options = {}
        options['detect_direction'] = 'true'
        options['probability'] = 'true'

        """ 带参数调用通用文字识别, 图片参数为本地图片 """
        # 采用高精度的
        img = client.basicAccurate(image, options)
        code = img['words_result'][0]['words']
        return code
# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from selenium import webdriver
import time
from scrapy.http.response.html import HtmlResponse

class SeleniumDownloadMiddleware(object):

    def __init__(self):
        #使用selenium+chromedriver的方式来处理通过ajax请求得到的数据
        # 本地定义一个profile文件夹，再通过ChromeOptions定义，再使用add_argument方法，指定'user-data-dir'的路径
        options = webdriver.ChromeOptions()
        options.add_argument('user-data-dir=F:\profile')
        #设置驱动
        self.driver = webdriver.Chrome(chrome_options=options)

    def process_request(self,request,spider):
        #请求数据
        self.driver.get(request.url)
        #设置时延，防止元素还没有加载出来
        time.sleep(3)

        #获取专题的时候，处理点击“展示更多”，这个展示更多，有可能有多个，不确定，但是需要一直点击它，直到没有这个按钮了
        try:
            while True:
                show_more = self.driver.find_element_by_xpath('//a[@class="show-more"]')
                show_more.click()
                time.sleep(0.3)
                #如果没有获取到按钮后，就退出这个操作
                if not show_more:
                    break
        except Exception as e:
            #假设本来就很少专题，没有展示更多的按钮，可以直接跳过
            pass
            print(e)

        #获取源代码
        source = self.driver.page_source
        #通过response对象处理source数据，然后返回给爬虫
        response = HtmlResponse(url=self.driver.current_url,body=source,request=request,encoding='utf-8')  #body传的是bytes数据类型，还需要编码一下
        return response

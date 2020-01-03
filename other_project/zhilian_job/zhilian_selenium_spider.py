# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/12/7 4:15

import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from lxml import html
from selenium.webdriver.common.by import By

class ZhiLian_selenium_spider(object):

    def __init__(self):
        # 本地定义一个profile文件夹，再通过ChromeOptions定义，再使用add_argument方法，指定'user-data-dir'的路径为我们创建的profile文件夹路径，最后再Chrome方法里面调用chrome_options就可以了
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=F:\profile')
        self.driver = webdriver.Chrome(chrome_options=self.options)
        #这里的url就是浏览器上面地址框的url，不是ajax数据的那个url
        self.url = 'https://sou.zhaopin.com/?jl=489&kw=%E5%AE%89%E5%85%A8%E6%B8%97%E9%80%8F&kt=3'
        # 定义一个空列表来保存所有的职位信息
        self.positions = []

    def run(self):

        self.driver.get(self.url)
        while True:
            #通过显示等待来确保，页面元素被加载到，可以获取到正常的源代码
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,'//div[@class="contentpile__content__wrapper__item__info__box__jobname jobName"]/span')))

            #获取每一页的职位源代码
            source = self.driver.page_source
            self.parse_list_page(source)
            try:
                #这里相当于只是获取了第一页的数据，爬完一页数据，需要点击跳转到下一页，获取数据
                next_button = self.driver.find_element_by_xpath('//button[@class="btn soupager__btn"]')
                # 这里需要增加一个判断，如果是最后一页，下一页的按钮就无法点击了(最后一页的class属性是btn soupager__btn soupager__btn--disable，因此判断这个属性值是否在下一页的class属性中，在就不执行下一页，不在，就执行下一页)
                if 'btn soupager__btn soupager__btn--disable' in next_button.get_attribute('class'):
                    break
                else:
                    next_button.click()   # 这里每一页都要点击一次也是不科学，可以通过死循环来处理，知道最后一页才跳出来，这样更好一点
            except:
                print(source)
            # 爬完一页数据后，睡眠1秒
            time.sleep(1)

    def parse_list_page(self,source):

        #根据获取到的每一页职位信息的源代码，进行获取每一页所有职位的url
        html_zhilian = html.etree.HTML(source)
        position_urls = html_zhilian.xpath('//a[@class="contentpile__content__wrapper__item__info"]/@href')
        for position_url in position_urls:
            self.request_position_detail(position_url)
            time.sleep(1)

    def request_position_detail(self,url):

        #根据得到的每一页的所有职位url，获取每一个职位的详情页面的源代码.这里该注意的是，职位列表页面需要保留，这里的职位详情页面需要重新打开一个新窗口操作
        self.driver.execute_script("window.open('%s')" % url)
        #这里需要切换句柄到新窗口，驱动也需要切换
        self.driver.switch_to_window(self.driver.window_handles[1])

        # 通过显示等待来确保，页面元素被加载到，可以获取到正常的源代码
        # 注意，presence_of_element_located方法只能去寻找一些元素，不能寻找那些文本，这个xpath语法://div[@class="new-info"]//h1/text()，需要去掉text(),这样才能让元素被获取到
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,'//div[@class="new-info"]//h1')))

        source = self.driver.page_source
        #把source源代码传给解析函数
        self.parse_position_detail(source)

        # 获取完职位详情页面后，关闭当前这个详情页
        self.driver.close()
        # 继续切换窗口和驱动回职位列表页面
        self.driver.switch_to_window(self.driver.window_handles[0])

    def parse_position_detail(self,source):

        #解析职位详情页面的数据，得到我们想要的数据
        html_position = html.etree.HTML(source)

        #职位名称
        position_name = html_position.xpath('//div[@class="new-info"]//h1/text()')[0]

        #薪水
        salary = html_position.xpath('//div[@class="l info-money"]/strong/text()')[0]

        #公司名称
        company_name = html_position.xpath('//div[@class="company l"]/a/text()')[0]

        #工作城市，工作年限，学历要求,招聘人数详情
        desc = html_position.xpath('//div[@class="info-three l"]/span')

        #工作城市
        city_spans = desc[0]
        city = city_spans.xpath('.//text()')[0]

        #工作年限
        work_year_spans = desc[1]
        work_year = work_year_spans.xpath('.//text()')[0]

        #学历要求
        education_spans = desc[2]
        education = education_spans.xpath('.//text()')[0]

        #招聘人数
        recruiting_number_spans = desc[3]
        recruiting_number = recruiting_number_spans.xpath('.//text()')[0]

        #职位亮点
        position_advantage = html_position.xpath('//div[@class="pos-info-tit"]/div/span')

        #职位描述
        position_desc = html_position.xpath('//div[@class="pos-ul"]//text()')
        #转换为字符串处理
        position_desc = ''.join(position_desc).strip()


        #定义一个字典来保存一个职位的数据
        position = {

            'position_name' : position_name ,
            'salary': salary,
            'company_name': company_name,
            'city': city,
            'work_year': work_year,
            'education': education,
            'recruiting_number': recruiting_number,
            'position_advantage' : position_advantage,
            'position_desc' : position_desc

        }
        self.positions.append(position)
        print(position)

if __name__ == '__main__':

    zhilian_spider = ZhiLian_selenium_spider()
    zhilian_spider.run()
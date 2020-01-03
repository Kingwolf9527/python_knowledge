# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/12/7 1:59

from selenium import webdriver
from lxml import html
import re
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Lagou_selenium_spider(object):

    def __init__(self):

        # 本地定义一个profile文件夹，再通过ChromeOptions定义，再使用add_argument方法，指定'user-data-dir'的路径为我们创建的profile文件夹路径，最后再Chrome方法里面调用chrome_options就可以了
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=F:\profile')
        self.driver = webdriver.Chrome(chrome_options=self.options)
        #这里的url就是浏览器上面地址框的url，不是ajax数据的那个url
        self.url = 'https://www.lagou.com/jobs/list_%E5%AE%89%E5%85%A8%E6%B8%97%E9%80%8F?px=default&city=%E5%85%A8%E5%9B%BD#filterBox'
        #定义一个空列表来保存所有的职位信息
        self.positions = []

    def run(self):

        self.driver.get(self.url)   #点击下一页获取数据，这个请求是不需要重新请求的
        while True:
            # 获取每一页的elements页面的源代码数据
            # 通过驱动的方式获取源代码跟直接在网页上，右键查看源代码是不同的，因为这些数据都是通过ajax请求的，网页的源代码是查看不了的，但是通过驱动方式，获取的源代码跟网页的elements获取的源代码是一样，可以获取到ajax数据的
            source = self.driver.page_source

            #防止下一页的按钮，没有及时加载处理，会报错，采用显式等待的方法,10秒超时，直到找到下一页按钮的定位
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="pager_container"]/span[last()]')))

            # 调用解析函数
            self.parse_list_source(source)

            try:
                # 这里相当于只是获取了第一页的数据，爬完一页数据，需要点击跳转到下一页，获取数据
                next_button = self.driver.find_element_by_xpath('//div[@class="pager_container"]/span[last()]')

                # 这里需要增加一个判断，如果是最后一页，下一页的按钮就无法点击了(最后一页的class属性是pager_next pager_next_disabled，因此判断这个属性值是否在下一页的class属性中，在就不执行下一页，不在，就执行下一页)
                if 'pager_next pager_next_disabled' in next_button.get_attribute('class'):
                    break
                else:
                    next_button.click()  # 这里每一页都要点击一次也是不科学，可以通过死循环来处理，知道最后一页才跳出来，这样更好一点
            except:
                print(source)
            #爬完一页数据后，睡眠1秒
            time.sleep(1)



    def parse_list_source(self,source):

        html_lagou = html.etree.HTML(source)
        #获取一页数据的所有职位url
        position_urls = html_lagou.xpath('//div[@class="p_top"]/a/@href')
        for position_url in position_urls:
            #请求每一个职位的url
            self.request_detail_page(position_url)
            #防止被ban掉ip
            time.sleep(1)


    def request_detail_page(self,url):

        #因为需要保持两个页面，所有需要用到switch_to_window，来切换窗口和驱动，需要再职位列表页和职位详情页不断的切换
        self.driver.execute_script("window.open('%s')" %url)
        self.driver.switch_to_window(self.driver.window_handles[1])

        #通过显示等待来确保，页面元素被加载到，可以获取到正常的源代码
        #注意，presence_of_element_located方法只能去寻找一些元素，不能寻找那些文本，这个xpath语法://div[@class="job-name"]/span/text()，需要去掉text(),这样才能让元素被获取到
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="job-name"]/span')))

        #获取每一个职位详情页面的源代码
        source = self.driver.page_source
        self.parse_detail_page(source)

        #获取玩职位详情页面后，关闭当前这个详情页
        self.driver.close()
        #继续切换窗口和驱动回职位列表页面
        self.driver.switch_to_window(self.driver.window_handles[0])

    def parse_detail_page(self,source):

        #根据上一个函数获取到每一个职位详情页面的源代码，进行解析，获取每一个职位的数据
        html_position = html.etree.HTML(source)

        # 职位名称
        position_name = html_position.xpath('//div[@class="job-name"]/span/text()')[0]

        # 工作经验，薪水，学历要求，工作地点详情
        descs = html_position.xpath('//dd[@class="job_request"]//span')

        # 薪水
        salary_spans = descs[0]
        salary = salary_spans.xpath('.//text()')[0]

        # 工作地点
        city_spans = descs[1]
        city = city_spans.xpath('.//text()')[0]
        # 使用正则处理一下不需要的符合和空格
        city = re.sub(r'[\s/]', '', city).strip()

        # 工作经验
        work_year_spans = descs[2]
        work_year = work_year_spans.xpath('.//text()')[0]
        work_year = re.sub(r'[\s/]', '', work_year).strip()

        # 学历要求
        education_spans = descs[3]
        education = education_spans.xpath('.//text()')[0]
        education = re.sub(r'[\s/]', '', education).strip()

        # 职位诱惑
        position_advantage = html_position.xpath('//dd[@class="job-advantage"]/p/text()')[0]

        # 职位描述
        position_desc = html_position.xpath('//dd[@class="job_bt"]//p/text() | //dd[@class="job_bt"]//p/span/text()')
        # 转为字符串的形式(''.join(列表))
        position_desc = ''.join(position_desc).strip()

        #公司名称
        company_name = html_position.xpath('//h2[@class="fl"]/text()')[0].strip()

        #定义一个字典来保存一个职位的数据
        position = {

            'company_name' : company_name,
            'name' : position_name,
            'salary' : salary,
            'city' : city,
            'work_year' : work_year,
            'education' : education,
            'position_advantage' : position_advantage,
            'position_desc' : position_desc
        }
        self.positions.append(position)
        print(position)
        print('='*50)

if __name__ == '__main__':
    lagou = Lagou_selenium_spider()
    lagou.run()



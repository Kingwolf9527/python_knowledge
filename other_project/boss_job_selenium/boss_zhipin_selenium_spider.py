# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/12/11 19:11

from selenium import webdriver
import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import html
import pymysql
from db_config import DB_config as df

class Boss_zhipin_spider(object):

    def __init__(self):
        # 本地定义一个profile文件夹，再通过ChromeOptions定义，再使用add_argument方法，指定'user-data-dir'的路径为我们创建的profile文件夹路径，最后再Chrome方法里面调用chrome_options就可以了
        options = webdriver.ChromeOptions()
        options.add_argument('user-data-dir=F:\profile')
        self.driver = webdriver.Chrome(chrome_options=options)
        self.Domain = 'https://www.zhipin.com'
        self.url = 'https://www.zhipin.com/c100010000/?query=%E5%AE%89%E5%85%A8%E6%B8%97%E9%80%8F&page=1&ka=page-1'

        #创建一个空列表来存储职位详情
        self.positions = []


    def run(self):

        #获取每一页的源代码
        self.driver.get(self.url)

        #需要处理下一页的问题，通过点击下一页的按钮，访问下一页，当最后一页的时候，退出循环，而且采用死循环的形式执行get请求
        while True:
            #增加显式等待时间，保证获取源代码正确
            WebDriverWait(self.driver,40).until(EC.presence_of_element_located((By.XPATH,'//div[@class="job-title"]')))

            #获取源代码
            source = self.driver.page_source
            self.parse_list_page(source)

            try:
                # 定位到下一页的按钮，以及寻找最后一页的下一页按钮规律,当最后一页的时候，退出循环,
                next_button = self.driver.find_element_by_xpath('//div[@class="page"]/a[@ka="page-next"]')
                if 'next disabled' in next_button.get_attribute('class'):           #这里获取的属性是下一页按钮的属性
                    break
                else:
                    next_button.click()
            except:
                print(source)

            # 爬完一页数据后，睡眠1秒
            time.sleep(1)

    def parse_list_page(self,source):
        #获取每一页的所有职位url
        html_page_position_urls = html.etree.HTML(source)
        position_urls = html_page_position_urls.xpath('//div[@class="info-primary"]//a/@href')
        urls = map(lambda url:self.Domain+url,position_urls)
        for url in urls:
            self.request_position_url(url)

    def request_position_url(self,url):
        #获取每一个职位详情页面的源代码,需要新打开一个窗口，用于切换，不能直接get请求，这样会覆盖职位列表页面
        self.driver.execute_script("window.open('%s')" %url)
        #切换新窗口和驱动
        self.driver.switch_to.window(self.driver.window_handles[1])

        #同样在获取源代码之前增加显式等待
        WebDriverWait(self.driver,40).until(EC.presence_of_element_located((By.XPATH,'//div[@class="info-company"]/h3/a')))

        #获取职位详情页面的源代码
        source = self.driver.page_source
        self.parse_position(source)

        #获取玩一个职位详情页面的源代码后，关闭掉，而且把窗口和驱动切换到职位列表页面中，继续获取职位详情
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])

    def parse_position(self,source):

        #解析职位详情页面的源代码，获取我们需要的数据
        html_position = html.etree.HTML(source)

        #公司名称
        company_name = html_position.xpath('//div[@class="info-company"]/h3/a/text()')[0]

        #职位名称
        position_name = html_position.xpath('//div[@class="name"]/h1/text()')[0]

        #薪水
        salary = html_position.xpath('//div[@class="info-primary"]/div[@class="name"]/span/text()')[0]
        salary = salary.strip()

        #工作城市，工作经验，学历要求
        descs = html_position.xpath('//div[@class="info-primary"]/p/text()')

        #工作城市
        city = descs[0]
        city = re.sub(r'城市：','',city)

        #工作经验
        work_year = descs[1]
        work_year = re.sub(r'经验：','',work_year)

        #学历要求
        education = descs[2]
        education = re.sub(r'学历：','',education)

        #职业描述
        positon_descs = html_position.xpath('//div[@class="job-sec"]/div[@class="text"]//text()')
        #转为字符串形式
        positon_descs = ''.join(positon_descs).strip()

        #团队介绍，公司优势
        advantage = html_position.xpath('//div[@class="job-sec"]/div[@class="job-tags"]/span/text()')

        #公司介绍
        introduce = html_position.xpath('//div[@class="job-sec company-info"]/div//text()')
        introduce = ''.join(introduce).strip()

        #工作地址
        work_address = html_position.xpath('//div[@class="location-address"]/text()')[0]

        #用一个字典来存储所有职位数据
        position = {
                'company_name' : company_name,
                'position_name': position_name,
                'salary': salary,
                'city': city,
                'work_year': work_year,
                'education': education,
                'positon_descs': positon_descs,
                'advantage': advantage,
                'introduce': introduce,
                'work_address': work_address
        }
        self.positions.append(position)
        print(position)
        time.sleep(1)

        self.mysql_position(position)

    def mysql_position(self, position):

        #连接数据库
        try:
            connect = pymysql.connect(host=df['host'],port=df['port'],user=df['user'],passwd=df['password'],database=df['db'],charset=df['charset'])
            cur = connect.cursor()
            # 使用 execute()  方法执行 SQL 插入数据
            sql = """

                 insert into boss_zhipin(company_name,position_name,salary,city,work_year,education,positon_descs,advantage,introduce,work_address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)

             """
            company_name = position['company_name']
            position_name = position['position_name']
            salary = position['salary']
            city = position['city']
            work_year = position['work_year']
            education = position['education']
            positon_descs = position['positon_descs']
            advantage = position['advantage']
            introduce = position['introduce']
            work_address = position['work_address']

            try:
                # 执行SQL插入语句
                cur.execute(sql, (str(company_name),
                                  str(position_name),
                                  str(salary),
                                  str(city),             #因为我设计的表结构都是varchar类型，所以，所以数据都是字符串才能保存到数据库，因为advantage字段获取到的每一个元素都是list，存不进数据库，需要转为str处理
                                  str(work_year),
                                  str(education),
                                  str(positon_descs),
                                  str(advantage),
                                  str(introduce),
                                  str(work_address)
                                  )
                            )
                # 提交到数据库执行
                connect.commit()
            except pymysql.Error as e:
                print(e)
                # 如果发生错误则回滚
                connect.rollback()
            # 关闭连接
            connect.close()
        except:
            print('数据库连接失败')


if __name__ == '__main__':


    boss_zhipin = Boss_zhipin_spider()
    boss_zhipin.run()
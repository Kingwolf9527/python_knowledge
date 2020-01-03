# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/1/21 1:31

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from lxml import html
import re
import pymysql
from db_config import DB_config as df

class JD_search_mainboard(object):

    def __init__(self):
        #配置驱动等等信息
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=F:\profile')
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.url = 'https://search.jd.com/search?keyword=%E4%B8%BB%E6%9D%BF&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=1.rem.0.0&cid3=681#J_searchWrap'

    def get_page_source(self):
        #获取每一页的源代码
        self.driver.get(self.url)

        # 需要处理下一页的问题，通过点击下一页的按钮，访问下一页，当最后一页的时候，退出循环，而且采用死循环的形式执行
        while True:

            # 增加显式等待时间，保证获取源代码正确
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH,'//div[@class="crumbs-nav-item"]/strong')))

            #获取源代码
            source = self.driver.page_source
            #传给解析每一页源代码的函数处理，提取url
            self.get_urls_page_source(source)

            try:
                #下一页处理
                next_button = self.driver.find_element_by_xpath('//span[@class="p-num"]/a[@class="pn-next"]')
                if 'pn-next disabled' in next_button.get_attribute('class'):
                    break
                else:
                    next_button.click()
            except:
                print(source)

            #没爬完一页，延时2秒
            time.sleep(2)

    def get_urls_page_source(self,source):

        #获取每一页的所有商品的url
        html_mainboard = html.etree.HTML(source)
        urls = html_mainboard.xpath('//div[contains(@class,"gl-i-wrap")]/div[@class="p-name p-name-type-2"]/a/@href')
        for url in urls:
            if 'https' not in url:
                url = 'https:' + url
            self.detail_page_source(url)

    def detail_page_source(self,url):

        #获取每个商品的源代码，需要新打开一个tab页,用于切换窗口，获取完成后，就关闭，再打开新的
        self.driver.execute_script("window.open('%s')" %url)
        print(url)
        # 切换新窗口和驱动
        self.driver.switch_to.window(self.driver.window_handles[1])

        # 增加显式等待时间，保证获取源代码正确
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="follow J-follow-shop"]/span')))

        #获取商品详情页面的源代码
        detail_source = self.driver.page_source
        self.parse_detail_source(detail_source,url)

        #获取一个商品的源代码后，就关闭，而且把窗口和驱动切换到搜索页面中，继续获取商品详情
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(0.5)

    def parse_detail_source(self,detail_source,url):

        html_mainboard_ = html.etree.HTML(detail_source)

        #创建一个字典来存储数据
        product = {}

        #详情页面的url，方便定位问题所在
        product['url'] = url

        #主板标题
        model = html_mainboard_.xpath('//div[@class="sku-name"]//text()')
        model = ''.join(model).strip()
        product['model'] = model

        #价格
        price = html_mainboard_.xpath('//div[@class="dd"]/span[contains(@class,"p-price")]//text()')
        price = ''.join(price).strip()
        product['price'] = price

        #累计评价
        comment = html_mainboard_.xpath('//div[@class="comment-count item fl"]/a/text()')[0]
        product['comment'] = comment

        #主板品牌
        mainboard_ = html_mainboard_.xpath('//ul[@id="parameter-brand"]/li/a/text()')
        if mainboard_:
            mainboard_type = mainboard_[0]
            product['mainboard_type'] = mainboard_type
        else:
            product['mainboard_type'] = '暂无数据'

        #其他商品信息
        infos = html_mainboard_.xpath('//ul[contains(@class,"parameter2 p-parameter-list")]/li/text()')
        for info in infos:
            #因为有部分参数，有的页面没有，需要处理
            if '商品名称' in info:
                # 主板名称
                name = re.sub(r'商品名称：','',info)
                product['name'] = name
            elif '商品毛重' in info:
                #商品毛重
                weight = re.sub(r'商品毛重：','',info)
                product['weight'] = weight
            elif '商品产地' in info:
                #商品产地
                origin_goods = re.sub(r'商品产地：','',info)
                product['origin_goods'] = origin_goods
            elif '应用场景' in info:
                #应用场景
                scenario = re.sub(r'应用场景：','',info)
                product['scenario'] = scenario
            elif '芯片' in info:
                #芯片类型
                chip_type = re.sub(r'INTEL芯片：|AMD芯片：','',info)
                product['chip_type'] = chip_type
            elif '板型' in info:
                #板型
                atx = re.sub(r'板型：','',info)
                product['atx'] = atx
            elif '接口' in info:
                #适用CPU接口
                cpu_interface = re.sub(r'适用CPU接口：|接口：','',info)
                product['cpu_interface'] = cpu_interface
            elif '游戏特色' in info:
                #游戏特色
                feature = re.sub(r'游戏特色：','',info)
                product['feature'] = feature
            else:
                product['origin_goods'] = '暂无数据'
                product['scenario'] = '暂无数据'
                product['chip_type'] = '暂无数据'
                product['cpu_interface'] = '暂无数据'
                product['atx'] = '暂无数据'
                product['feature'] = '暂无数据'


        print(product)
        self.mainboard_pymysql(product)

    def mainboard_pymysql(self,product):

        # 连接数据库
        connect = pymysql.connect(
            host=df['host'],
            port=df['port'],
            user=df['user'],
            password=df['password'],
            database=df['db'],
            charset=df['charset']
        )
        #设置游标
        cur = connect.cursor()
        #插入语句的SQL
        sql = """
            insert into mainboard(url,model,price,comment,mainboard_type,name,weight,origin_goods,scenario,chip_type,atx,cpu_interface,feature)\
            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        try:
             #执行SQL
            cur.execute(sql,
                             (product['url'],product['model'],product['price'],product['comment'],product['mainboard_type'],product['name'],product['weight'],product['origin_goods'],product['scenario'],product['chip_type'],product['atx'],product['cpu_interface'],product['feature'])
                            )
             # 提交到数据库执行
            connect.commit()
        except pymysql.Error as e:
            print(e)
            #如果发生错误则回滚
            connect.rollback()
        finally:
            cur.close()
            connect.close()

if __name__ == '__main__':
    mainboard = JD_search_mainboard()
    mainboard.get_page_source()


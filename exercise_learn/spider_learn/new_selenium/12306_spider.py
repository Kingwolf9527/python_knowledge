# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/12/12 4:10

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Qiangpiao(object):

    def __init__(self):
        # 本地定义一个profile文件夹，再通过ChromeOptions定义，再使用add_argument方法，指定'user-data-dir'的路径为我们创建的profile文件夹路径，最后再Chrome方法里面调用chrome_options就可以了
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=F:\profile')
        self.driver = webdriver.Chrome(chrome_options=self.options)
        #登录的url
        self.login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
        #
        self.personal_centre_url = 'https://kyfw.12306.cn/otn/view/index.html'
        self.search_ticket_url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'

    def _login(self):
        self.driver.get(self.login_url)
        self.driver.find_element_by_link_text(r'账号登录').click()
        #显式等待，判断是否登录成功(EC.url_to_be(目标url)：判断当前url是否等于目标url，是就不继续等待下去了，退出)
        WebDriverWait(self.driver,1000).until(EC.url_to_be(self.personal_centre_url))
        print('登录成功')

    def _order_ticket(self):
        pass

    def run(self):
        self._login()
        self._order_ticket()

if __name__ == '__main__':

    spider = Qiangpiao()
    spider.run()
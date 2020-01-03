# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/2/24 3:16

'''

    页面基础类，用于所有页面的继承


'''

from maizi_test.util.get_driver import openBrower

class Page(object):

    def __init__(self):
        self.login_url = 'http://www.maiziedu.com/'
        self.driver = openBrower()

    def open(self):
        self.driver.get(self.login_url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def script(self,js):
        return self.driver.execute_script(js)
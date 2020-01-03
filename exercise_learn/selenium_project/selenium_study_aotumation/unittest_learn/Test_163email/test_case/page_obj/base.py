# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/1/31 17:04

class Page(object):

    '''

    页面基础类，用于所有页面的继承

    '''

    login_url = 'https://email.163.com/'

    def __init__(self,driver,base_url=login_url,parent=None):
        self.driver = driver
        self.base_url = base_url
        self.parent = parent
        self.timeout = 30

    def _open(self):
    # def _open(self, url)     #其他情况再处理
        #url = self.base_url + url
        self.driver.get(self.base_url)
        assert self.on_page(),'Did not land on %s' %self.base_url

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def open(self):
        # self._open(self.url)
        self._open()

    def on_page(self):
        # return self.driver.current_url == self.base_url + self.url
        return self.driver.current_url == self.base_url

    def script(self,src):
        return self.driver.execute_script(src)


# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/6 6:19

from new_maizi_aututest.utils.jump_login import Jump_login
from new_maizi_aututest.utils.browser import BrowserEngine

class Login(object):

    def __init__(self,driver):
        self.driver = driver

    def Login(self):
        browser = BrowserEngine()
        self.driver = browser.open_browser()
        account_info = Jump_login(self.driver)
        #跳转登录页面
        account_info.jump()
        #用户登录
        account_info.login('13726229967','922521dfxs')
        return self.driver



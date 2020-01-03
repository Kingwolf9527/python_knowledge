# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/2/19 1:41

import unittest
from .driver import browser


class Mytest(unittest.TestCase):

    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.url = 'https://email.163.com/'

    def tearDown(self):
        self.driver.quit()
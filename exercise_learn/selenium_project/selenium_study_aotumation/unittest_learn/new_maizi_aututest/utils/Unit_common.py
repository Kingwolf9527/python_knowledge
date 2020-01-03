# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/5 7:26

import unittest
from new_maizi_aututest.utils.browser import BrowserEngine

class Mytest(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine()
        self.driver = browser.open_browser()
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()
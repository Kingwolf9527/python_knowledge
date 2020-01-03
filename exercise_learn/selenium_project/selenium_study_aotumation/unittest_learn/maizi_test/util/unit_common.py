# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/2/24 3:20

import unittest
from .get_driver import openBrower


class Mytest(unittest.TestCase):

    def setUp(self):
        #调用驱动
        self.driver = openBrower()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

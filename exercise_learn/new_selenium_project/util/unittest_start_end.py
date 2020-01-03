# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/12/7 5:35

import unittest
import time
from util.browser_driver_test import Webdriver_Browser
from businessview.register_business import Register_Business
from util.common_log import Common_Logs


#实例化logger
log_name = Common_Logs(logger='Unittest_switch')
logger = log_name.get_logger()

class Unittest_start_end(unittest.TestCase):

    def setUp(self):

        #打开浏览器以及访问对应网站
        self.browser = Webdriver_Browser('Browser','chrome_browser')
        self.browser.get_init_url('Register_url','url')
        self.driver = self.browser.driver

        #实例化business方法
        self._register_ = Register_Business(self.driver)

    def tearDown(self):

        time.sleep(2)
        logger.info('------ close the browser    ------')
        self.driver.quit()

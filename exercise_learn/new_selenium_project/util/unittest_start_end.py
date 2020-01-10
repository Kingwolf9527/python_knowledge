# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/12/7 5:35

import unittest
import time
from new_selenium_project.util.browser_driver_test import WebdriverBrowser
from new_selenium_project.PageObject.businessview.register_business import Register_Business
from new_selenium_project.util.common_log import Common_Logs


#实例化logger
log_name = Common_Logs(logger='Unittest_switch')
logger = log_name.get_logger()

class UnittestStartEnd(unittest.TestCase):

    def setUp(self):

        #打开浏览器以及访问对应网站
        self.browser = WebdriverBrowser('Browser','chrome_browser')
        self.browser.getUrl('Register_url','url')
        self.driver = self.browser.getDriver()

        #实例化business方法
        self.new_register_ = Register_Business(self.driver)

    def tearDown(self):

        time.sleep(2)
        logger.info('------ close the browser    ------')
        self.driver.quit()

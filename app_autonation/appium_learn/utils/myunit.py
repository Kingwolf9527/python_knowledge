# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/4/7 5:49

from appium_learn.utils.driver import Driver
from appium_learn.utils.common_logs import Common_log
import time
import unittest

logger = Common_log(logger='common_start_unittest').get_logger()

class Common_start(unittest.TestCase):

    def setUp(self):
        logger.info('===================setup======================')
        self.driver = Driver().read_caps()

    def tearDown(self):
        logger.info('====================teardown==========================')
        time.sleep(5)
        #关闭app
        self.driver.close_app()
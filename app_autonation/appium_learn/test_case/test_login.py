# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/4/7 5:55

from appium_learn.utils.common_logs import Common_log
from appium_learn.utils.myunit import Common_start
from appium_learn.page_object.common_login import Common_login
import unittest

logger = Common_log(logger='test_login').get_logger()

class Test_login(Common_start):

    def test_username_pwd_success(self):
        logger.info('=======================username and password right=======================')
        login = Common_login(self.driver)
        login.login_check(username='kingwolfbook14',password='922521dfxs')


    def test_pwd_error(self):
        logger.info('=========================username is right,password is wrong================================================')
        login = Common_login(self.driver)
        login.login_check(username='kingwolfbook14',password='123456')


    def test_username_error(self):
        logger.info('=========================username is invalid================================================')
        login = Common_login(self.driver)
        login.login_check(username='king',password='123456')


if __name__ == '__main__':
    unittest.main()

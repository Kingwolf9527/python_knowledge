# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/4/23 4:09

from kyb_project_test.utils.common_logs import Common_log
from kyb_project_test.page_object.businessView.register_view import Register_View
from kyb_project_test.utils.myunit import Common_start
import random
import unittest

logger = Common_log(logger='register test').get_logger()

class Register(Common_start):

    def test_register(self):
        logger.info('======================test user register=========================')
        info = Register_View(self.driver)

        username = 'king1' + str(random.randint(10000,50000))
        password = 'wolf1' + str(random.randint(10000,50000))
        email = 'CR7' + str(random.randint(100,500)) + '@163.com'

        juedge = info.register_action(username=username,password=password,email=email)
        self.assertTrue(juedge)

if __name__ == '__main__':
    unittest.main()


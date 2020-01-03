# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/4/23 4:21

from kyb_project_test.utils.common_logs import Common_log
from kyb_project_test.utils.myunit import Common_start
from kyb_project_test.page_object.businessView.login_view import Common_login
from kyb_project_test.utils.account_data import Account_data
import unittest

logger = Common_log(logger='test login').get_logger()

class Login_test(Common_start):
    #账号数据文件
    account_file = 'account.xlsx'

    def test_login_3_username_wrong(self):
        logger.info('====================test_login_username_wrong===========================')
        #账号，密码数据读取
        info = Account_data(data_file=self.account_file)
        userdata = info.get_sheetinfo_by_index(0)
        #错误账号，取第一组数据
        username = userdata[0]['account']
        password = userdata[0]['password']
        #调用登录方法
        user = Common_login(self.driver)
        user.login_check(username=username,password=password)
        login_status = user.login_status_check()
        #断言处理
        self.assertTrue(login_status,msg='login failed')

    def test_login_2_password_wrong(self):
        logger.info('====================test_login_password_wrong===========================')
        #账号，密码数据读取
        info = Account_data(data_file=self.account_file)
        userdata = info.get_sheetinfo_by_index(0)
        #错误账号，取第一组数据
        username = userdata[1]['account']
        password = userdata[1]['password']
        #调用登录方法
        user = Common_login(self.driver)
        user.login_check(username=username,password=password)
        login_status = user.login_status_check()
        #断言处理
        self.assertTrue(login_status,msg='login failed')


    def test_login_1_success(self):
        logger.info('====================test_login_success===========================')
        #账号，密码数据读取
        info = Account_data(data_file=self.account_file)
        userdata = info.get_sheetinfo_by_index(0)
        #错误账号，取第一组数据
        username = userdata[2]['account']
        password = userdata[2]['password']
        #调用登录方法
        user = Common_login(self.driver)
        user.login_check(username=username,password=password)
        login_status = user.login_status_check()
        #断言处理
        self.assertTrue(login_status)


if __name__ == '__main__':
    unittest.main()


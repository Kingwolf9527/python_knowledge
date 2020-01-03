# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/6 6:02

from new_maizi_aututest.page_object.login_link_text import Login_link_text
from new_maizi_aututest.page_object.common_login import Common_Login
from new_maizi_aututest.utils.log import LogDetail
import time

logger = LogDetail(logger='Jump_login').get_logger()

class Jump_login(object):

    def __init__(self,driver):
        self.driver = driver

    #跳转登录页面
    def jump(self):
        try:
            login_alert = Login_link_text(self.driver)
            login_alert.send_login_btn()
            time.sleep(2)
            try:
                assert '麦子学院' in login_alert.get_title()
                logger.info('assert success')
            except NameError as e:
                logger.error('assert Fail')
        except NameError as e:
            logger.error('Jump login Fail')

    def login(self,account,password):

        send_login = Common_Login(self.driver)
        #输入账号
        send_login.send_account(account)
        #输入密码
        send_login.send_password(password)
        #点击登录按钮
        send_login.click_button()
        time.sleep(3)



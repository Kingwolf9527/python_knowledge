# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/4/27 4:45

from kyb_project_test.utils.common_logs import Common_log
from kyb_project_test.config.read_configparser import Config_paser
import os

logger = Common_log(logger='email data').get_logger()

class Email_data(object):

    def __init__(self):
        self.cf = Config_paser()

    def email_info(self):
        """
        读取邮箱配置文件的相关参数
        :return:
        """
        host = self.cf.get_selectoin('email','host')
        account = self.cf.get_selectoin('email','email_account')
        license_key = self.cf.get_selectoin('email','license_key')
        receiver = self.cf.get_selectoin('email','receiver')
        email_title = self.cf.get_selectoin('email','email_title')
        email_content = self.cf.get_selectoin('email','email_content')

        return host,account,license_key,receiver,email_title,email_content
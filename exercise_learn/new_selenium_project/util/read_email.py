# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/12/7 3:37

import yagmail
import os
from util.read_config import Read_Config


class Read_Email(object):

    def __init__(self):

        #调用读取配置文件方法
        email_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config')
        email_config = os.path.join(email_dir, "email_info.ini")
        self.email_info = Read_Config(filename=email_config)

    def get_email_info(self):
        """
        读取邮箱配置文件的信息
        :return:
        """
        #发送邮件者
        sender = self.email_info.get_value('Email_info','sender')

        #发送邮箱者的授权码
        authorization_code = self.email_info.get_value('Email_info','authorization_code')

        #接收邮箱者
        receiver = self.email_info.get_value('Email_info','receiver')

        #SMTP配置
        smtp_server = self.email_info.get_value('Email_info','smtp_server')

        #邮件标题
        subject = self.email_info.get_value('Email_info','subject')

        #邮件正文
        contents = self.email_info.get_value('Email_info','contents')

        return sender,authorization_code,receiver,smtp_server,subject,contents


if __name__ == '__main__':
    test = Read_Email()
    email = test.get_email_info()
    print(email)
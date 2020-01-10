# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/12/7 3:37

import os
from new_selenium_project.util.read_config import Read_Config


class ReadEmail(object):

    def __init__(self):

        #调用读取配置文件方法
        emailDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config')
        emailConfig = os.path.join(emailDir, "email_info.ini")
        self.emailInfo = Read_Config(filename=emailConfig)

    def getEmailInfo(self):
        """
        读取邮箱配置文件的信息
        :return:
        """
        #发送邮件者
        sender = self.emailInfo.get_value('Email_info','sender')

        #发送邮箱者的授权码
        authorizationCode = self.emailInfo.get_value('Email_info','authorization_code')

        #接收邮箱者
        receiver = self.emailInfo.get_value('Email_info','receiver')

        #SMTP配置
        smtp_server = self.emailInfo.get_value('Email_info','smtp_server')

        #邮件标题
        subject = self.emailInfo.get_value('Email_info','subject')

        #邮件正文
        contents = self.emailInfo.get_value('Email_info','contents')

        return sender,authorizationCode,receiver,smtp_server,subject,contents


if __name__ == '__main__':
    test = ReadEmail()
    email = test.getEmailInfo()
    print(email)
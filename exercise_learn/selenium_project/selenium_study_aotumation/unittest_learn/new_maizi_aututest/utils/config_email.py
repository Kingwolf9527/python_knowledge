# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/10 4:28

import configparser
import os

class Email(object):

    def email_config(self):

        '''读取配置文件'''
        con_path = os.path.dirname(os.path.dirname(__file__))
        file_path = con_path + '/config/android_9_config.ini'
        cf = configparser.ConfigParser()
        cf.read(file_path,encoding='utf-8')

        # 同时获取邮件的相关配置信息
        host = cf.get('email','host')
        email_account = cf.get('email', 'email_account')
        license_key = cf.get('email', 'license_key')
        receiver = cf.get('email', 'receiver')
        email_title = cf.get('email', 'email_title')
        email_content = cf.get('email', 'email_content')
        return host,email_account,license_key,receiver,email_title,email_content

if __name__ == '__main__':
    t = Email()
    tt = t.email_config()
    print(tt)
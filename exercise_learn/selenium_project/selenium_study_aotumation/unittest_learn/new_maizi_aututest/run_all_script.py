# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/9 4:23

import unittest
import os
import yagmail
import time
from new_maizi_aututest.utils.package.HTMLTestRunner_PY3 import HTMLTestRunner
from new_maizi_aututest.utils.config_email import Email

#定义发送邮件，附带最新测试报告的附件
def send_email(new_file):
    #调用邮箱的配置方法
    email_class = Email()
    email = email_class.email_config()
    #读取邮箱的配置信息
    host = email[0]
    user = email[1]
    password = email[2]
    to = email[3]
    to = to.split(',')
    subject = email[4]
    contents = email[5]
    #发送邮件
    mail = yagmail.SMTP(user=user,password=password,host=host,smtp_ssl=True)
    mail.send(to=to,subject=subject,contents=contents,attachments=new_file)
    print('发送邮件完成！')

#查找测试报告目录，找到最新生成的测试报告文件
def new_report_file(report_dir):
    #获取测试报告目录下的所有文件和文件夹，返回一个列表
    file = os.listdir(report_dir)
    #对生成的测试报告进行排序，升序(通过文件的修改时间排序)
    file.sort(key=lambda x:os.path.getmtime(report_dir + '\\' + x))
    new_file = os.path.join(report_dir,file[-1])      #因为是升序，列表的最后一个文件是最新的
    return new_file

if __name__ == '__main__':

    #测试用例的路径
    case_dir = os.path.dirname(__file__) + '/test_case/'
    discover = unittest.defaultTestLoader.discover(start_dir=case_dir,pattern='test*.py')

    #测试报告的路径
    report_dir = os.path.dirname(__file__) + '/report/'
    #测试报告的名称规范
    now_time = time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))
    report_name = report_dir + now_time + '.html'
    with open(report_name,'wb') as f:
        report_runner = HTMLTestRunner(stream=f,\
                                       title='麦子学院的登录自动化测试报告',\
                                       description='用例执行情况：')
        report_runner.run(discover)

    #调用查找最新测试报告方法
    new_report = new_report_file(report_dir)
    #调用发送邮件方法
    send_email(new_report)
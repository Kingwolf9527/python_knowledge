# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/4/27 4:58

#使用sys把项目路径添加进去，为后续的bat脚本执行方便
import sys
sys.path.append(r'F:\GitExtensions_python')
sys.path.append(r'F:\GitExtensions_python\project_spider')
sys.path.append(r'F:\GitExtensions_python\project_spider\app_autonation')
sys.path.append(r'F:\GitExtensions_python\project_spider\app_autonation\appium_learn')
sys.path.append(r'F:\GitExtensions_python\project_spider\app_autonation\appium_learn\kyb_project_test')

import unittest
import os
import time
import yagmail
from kyb_project_test.utils.package.HTMLTestRunner_PY3 import HTMLTestRunner
from kyb_project_test.utils.common_logs import Common_log
from kyb_project_test.utils.email_data import Email_data


logger = Common_log(logger='run all script').get_logger()

class Run_script(object):

    def __init__(self):
        """
        调用邮箱的配置方法
        """
        self.email = Email_data()
        self.data = self.email.email_info()

    def send_email(self,new_report):
        """
        读取邮箱配置
        :param new_report:
        :return:
        """
        host = self.data[0]
        user = self.data[1]
        password = self.data[2]
        to = self.data[3]
        #这里可以设置多个接收者
        to = to.split(',')
        subject = self.data[4]
        contents = self.data[5]
        attachments = new_report
        #发送邮件
        try:
            mail = yagmail.SMTP(host=host,user=user,password=password,smtp_ssl=True)
            mail.send(to=to,subject=subject,contents=contents,attachments=attachments)
        except Exception as e:
            print('发送邮件失败，原因是: %s' %e)
        else:
            print('发送邮件成功！')

    def new_report_file(self,report_path):
        """
        生成测试报告，并且寻找最新的测试报告
        :param report_path:
        :return:
        """
        file = os.listdir(report_path)
        #按照文件的修改时间排序,升序(sort())
        file.sort(key=lambda x:os.path.getmtime(report_path + '\\' + x))
        new_report = os.path.join(report_path,file[-1])
        return new_report

if __name__ == '__main__':

    # 测试用例所在的文件夹
    test_case_dir = os.path.dirname(os.path.dirname(__file__)) + '/test_cases/'
    # 测试报告的文件夹
    report_dir = os.path.dirname(os.path.dirname(__file__)) + '/reports/'

    #加载所有测试用例
    discover = unittest.defaultTestLoader.discover(start_dir=test_case_dir,\
                                                   pattern='test*.py')
    #测试报告文件的命名规范
    now_time = time.strftime('%y-%m-%d %H_%M_%S',time.localtime(time.time()))
    #测试报告文件名
    report_name = report_dir + now_time + '.html'

    #测试报告写入内容
    with open(report_name,'wb') as f:
        report_runner = HTMLTestRunner(stream=f,\
                                       title='考研帮自动化测试报告',\
                                       description='用例执行情况：')
        report_runner.run(discover)

    #调用生成测试报告和发送邮件方法
    runner = Run_script()
    new_report = runner.new_report_file(report_path=report_dir)
    runner.send_email(new_report=new_report)
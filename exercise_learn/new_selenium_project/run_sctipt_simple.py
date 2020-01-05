# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/11/30 5:17

import sys
sys.path.append(r'F:\Tortoise_python\exercise_learn\new_selenium_project')

import unittest
import os
import time
import HTMLTestRunner_PY3
import yagmail
from util.read_email import Read_Email
from util.common_log import Common_Logs


#实例化logger
log_name = Common_Logs(logger='run_script')
logger = log_name.get_logger()

class RunCase(object):

    def test_exe_case(self):

        #获取case的目录
        case_path = os.path.join(os.path.dirname(__file__),'test_case')
        logger.info('------  case_path is: %s   ------' %case_path)
        #执行所有case文件
        suite = unittest.defaultTestLoader.discover(start_dir=case_path,pattern='test*.py')
        # unittest.TextTestRunner().run(suite)
        return suite

    def report_info(self):

        #实例化加载测试报告方法
        case_suite = self.test_exe_case()

        #测试报告的路径
        self.report_path = os.path.join(os.path.dirname(__file__),'report')
        logger.info('------  report_path is: %s   ------' %self.report_path)

        #测试报告的名字
        report_format =time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))
        report_dir = os.path.join(self.report_path,report_format)
        report_name = report_dir + '.html'
        logger.info('------ report_name is: %s    ------' %report_name)

        #往测试报告写入信息：
        with open(report_name,'wb') as f:
            #加载HTMLTestRunner_PY3
            report_result = HTMLTestRunner_PY3.HTMLTestRunner(stream=f,\
                                                              title='第三次测试报告',\
                                                              description='测试结果如下：')
            report_result.run(case_suite)


    def get_new_report(self,report_path):
        """
        查找最新的测试报告
        :param report_path: 测试报告所在的目录
        :return:
        """

        #返回测试报告目录页面的所有文件或者文件夹，结果是一个list
        file = os.listdir(self.report_path)

        #对测试报告排序(采用默认的asc)
        file.sort(key=lambda x:os.path.getmtime(self.report_path + '/' + x),reverse=False)

        #获取最新测试报告文件
        new_report = os.path.join(self.report_path,file[-1])
        logger.info('------ the new_report is: %s    ------' %new_report)

        return new_report

    def send_email(self, new_report):
        """
        调用email方法，得到配置信息，并且发送最新生成的测试报告
        :param report_new: 需要发送的最新测试报告---attachments(附件发送)
        :return:
        """
        # 发送邮件者
        sender = Read_Email().get_email_info()[0]
        # 发送邮箱者的授权码
        authorization_code = Read_Email().get_email_info()[1]
        # 接收邮箱者
        receiver = Read_Email().get_email_info()[2]
        # SMTP配置
        smtp_server = Read_Email().get_email_info()[3]
        # 邮件标题
        subject = Read_Email().get_email_info()[4]
        # 邮件正文
        contents = Read_Email().get_email_info()[5]

        # 获取最新测试报告
        new_report = self.get_new_report(self.report_path)

        # 发送邮件
        email = yagmail.SMTP(user=sender, password=authorization_code, host=smtp_server, smtp_ssl=True)
        email.send(to=receiver, subject=subject, contents=contents, attachments=new_report)
        logger.info('邮件发送完成！')


if __name__ == '__main__':
    # unittest.main()
    RUN = RunCase()
    RUN.report_info()
    tt = RUN.get_new_report(RUN.report_path)
    RUN.send_email(tt)
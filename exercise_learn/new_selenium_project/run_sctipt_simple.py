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

    def loadTestCase(self):

        #获取case的目录
        casePath = os.path.join(os.path.dirname(__file__),'test_case')
        logger.info('------  case_path is: %s   ------' %casePath)
        #执行所有case文件
        suite = unittest.defaultTestLoader.discover(start_dir=casePath,pattern='test*.py')
        # unittest.TextTestRunner().run(suite)
        return suite

    def reportInfo(self):

        #实例化加载测试报告方法
        caseSuite = self.loadTestCase()

        #测试报告的路径
        reportPath = os.path.join(os.path.dirname(__file__),'report')
        logger.info('------  report_path is: %s   ------' %reportPath)

        #测试报告的名字
        reportFormat =time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))
        reportDir = os.path.join(reportPath,reportFormat)
        reportName = reportDir + '.html'
        logger.info('------ report_name is: %s    ------' %reportName)

        #往测试报告写入信息：
        with open(reportName,'wb') as f:
            #加载HTMLTestRunner_PY3
            reportResult = HTMLTestRunner_PY3.HTMLTestRunner(stream=f,\
                                                              title='第三次测试报告',\
                                                              description='测试结果如下：')
            reportResult.run(caseSuite)

        return reportPath


    def getNewReport(self,reportPath):
        """
        查找最新的测试报告
        :param reportPath: 测试报告所在的目录
        :return:
        """
        #获取测试报告目录
        reportPath = self.reportInfo()

        #返回测试报告目录页面的所有文件或者文件夹，结果是一个list
        file = os.listdir(reportPath)

        #对测试报告排序(采用默认的asc)
        file.sort(key=lambda x:os.path.getmtime(reportPath + '/' + x),reverse=False)

        #获取最新测试报告文件
        newReport = os.path.join(reportPath,file[-1])
        logger.info('------ the new_report is: %s    ------' %newReport)

        return newReport

    def sendEmail(self, reportPath):
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
        new_report = self.getNewReport(reportPath)

        # 发送邮件
        email = yagmail.SMTP(user=sender, password=authorization_code, host=smtp_server, smtp_ssl=True)
        email.send(to=receiver, subject=subject, contents=contents, attachments=new_report)
        logger.info('邮件发送完成！')


if __name__ == '__main__':
    # unittest.main()
    test = RunCase()
    test.loadTestCase()
    test.reportInfo()
    test.getNewReport()
    test.sendEmail()

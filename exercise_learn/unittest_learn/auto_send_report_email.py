# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/18 2:57

from HTMLTestRunner_PY3 import HTMLTestRunner
import unittest
import time
import os
from email.mime.text import MIMEText
from email.header import Header
import smtplib

'''
    =================================定义发送邮件======================================
    
'''

def send_mail(file_new):

    # 第三方 SMTP 服务
    email_host = "smtp.163.com"  # 设置服务器
    email_user = "lccr777@163.com"  # 用户名
    email_passwd = "922521dfxs"  # 授权码

    # 发送邮箱
    Sender = "lccr777@163.com"
    # 接收邮箱
    Receiver = "1069645896@qq.com"  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    #打开接收过来的最新测试报告文件(是HTML文件)
    with open(file_new,'rb') as f:
        #邮件的正文
        mail_body = f.read().decode('utf-8')
        #发送HTML内容的邮件
        msg = MIMEText(mail_body,'html','utf-8')

        #邮件标题
        # subject = '自动化测试报告'
        msg['Subject'] = Header('自动化测试报告','utf-8')
        msg['From'] = Sender
        msg['To'] = Receiver

        Receiver = "1069645896@qq.com"  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        #发送邮件
        try:
            smtpObj = smtplib.SMTP_SSL()
            smtpObj.connect(email_host, 465)  # 25 为非SSL SMTP 端口号   SSL的端口：465/994
            smtpObj.set_debuglevel(1)  # 打印出和SMTP服务器交互的所有信息
            smtpObj.login(email_user, email_passwd)  # 登录发送者的邮箱
            smtpObj.sendmail(Sender, Receiver, msg.as_string())  # 发送邮件,msg必须是字符串类型
            smtpObj.quit()
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("邮件发送失败！")


'''
    ===============================查找测试报告目录，找到最新生成的测试报告文件=============================

'''
def new_report(test_report):

    #获取测试报告目录下的所有文件和文件夹,结果以列表形式返回
    lists = os.listdir(test_report)

    # 利用sort()方法，对目录下的文件以及文件夹按时间重新排序(sort(self, key=None, reverse=False))
    # [按key的关键字进行升序排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间，所以最终以文件时间从小到大排序]
    # 最后对lists元素，按文件修改时间大小从小到大排序
    # os.path.getatime(file)  # 输出最近访问时间1318921018.0
    # os.path.getctime(file)  # 输出文件创建时间
    # os.path.getmtime(file)  # 输出最近修改时间
    lists.sort(key=lambda fn:os.path.getmtime(test_report + "\\" + fn))

    # 获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
    file_new = os.path.join(test_report,lists[-1])
    print(file_new)
    return file_new


if __name__ == '__main__':

    # 定义测试用例所在的目录
    test_dir = "F:\\local_repository\Spider-learn\\new-spider-and-python\\new exercise\\unittest"

    #定义测试报告的目录
    test_report = "F:\\HTML_report"

    # 生成按照一定格式的当前时间，拼接到生成的测试报告的文件名中，防止因为没有修改文件名，导致旧数据被覆盖
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")
    report_file = test_report + "\\" + now_time + "result.html"

    # 加载测试用例
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

    # 生成测试报告
    with open(report_file, 'wb') as f:

        runner = HTMLTestRunner(stream=f,
                                verbosity=2,
                                title='测试报告',
                                description='执行人：Kingwolf')
        # run()的对象不再是unittest.TestSuite()，而是unittest.defaultTestLoader.discover()对象
        runner.run(discover)

        #调用获取最新文件的方法：new_report(new_report):获取最新测试报告目录下的最新文件,testreport传参就是前面定义的测试用例所在的目录,记住是获取目录
        report = new_report(test_report)

        #通过调用邮件方法--send_mail(file_new):邮件发送测试报告,file_new就是获取的最新修改的文件
        send_mail(report)






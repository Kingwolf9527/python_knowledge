# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/17 2:38

from selenium import webdriver
import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner
import time

class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.url = "http://www.baidu.com"

    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.url + '/')
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys('HTMLTestRunner')
        driver.find_element_by_id('su').click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':

    test_suite = unittest.TestSuite()
    test_suite.addTest(Baidu('test_baidu_search'))

    #按照一定时间获取当前时间(目的在于：防止下一次执行前，忘了修改文件名称，执行后，覆盖了旧的报告文件)
    now_time = time.strftime("%Y-%m-%d %H_%M_%M")
    file = "F:/HTML_report./" + now_time + "result.html"

    #定义报告存放的路径
    with open(file,'wb') as f:
        #定义测试报告-HTMLTestRunner(self, stream=sys.stdout, verbosity=1, title=None, description=None)的用法
        runner = HTMLTestRunner(stream=f,
                                verbosity=2,
                                title="百度搜索的测试报告",
                                description="用例执行情况：")
        #运行测试用例
        runner.run(test_suite)
# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/12/1 3:44

import unittest
import os
# from util.browser_driver_test import driver_init
import HTMLTestRunner_PY3


class MyTestCase(unittest.TestCase):# 继承unittest.TestCase

    # @classmethod
    # def setUpClass(cls):
    #     # 必须使用 @classmethod 装饰器,所有test运行前运行一次
    #     print('这是所有case的前置条件')
    #
    # @classmethod
    # def tearDownClass(cls):
    #     # 必须使用 @classmethod 装饰器, 所有test运行完后运行一次
    #     print('这是所有case的后置条件')

    def setUp(self):
        # 每个测试用例执行之前的操作
        # self.driver = driver_init(0)
        print('这是03每条case的前置条件')

    def tearDown(self):
        # 每个用例执行之后的操作
        # # 捕获异常
        # for method_name, error in self._outcome.errors:
        #     if error:
        #         #获取当前报错的case名字
        #         case_name = self._testMethodName
        #         #保存错误信息的截图位置
        #         error_image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'/images/')
        #         self.driver.get_screenshot_as_file(error_image_path + case_name+ '.png')
        print('这是03每条case的后置条件')

    def test_Third(self):  # 测试用例的命名必须以test开头，否则不予执行
        self.assertTrue(2>5,'测试结果为false，case失败')
        print('03: 第三条case')

    def test_First(self):
        print('01: 第一条case')

    @unittest.skip('不执行这条case')  # 跳过这条case
    def test_Second(self):
        print('02: 第二条case')

    def test_Fourth(self):
        print('04: 第四条case')


if __name__ == '__main__':
    unittest.main() # 使用main()直接运行时，将按case的名称顺序执行
    # suite = unittest.TestSuite()
    # suite.addTest(MyTestCase("test_Third"))  # 将需要执行的case添加到Test Suite中，没有添加的不会被执行
    # suite.addTest(MyTestCase("test_Second"))
    # suite.addTest(MyTestCase("test_First"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)  # 将根据case添加的先后顺序执行
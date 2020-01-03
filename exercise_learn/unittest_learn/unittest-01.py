# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/16 4:40

import unittest

class Test(unittest.TestCase):

    def setUp(self):
        number = input("请输入一个数字：")
        self.number = int(number)


    def test_case(self):
        self.assertEqual(self.number,10,msg="您输入的不是10！")
        self.assertIsNone()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()



'''
    setUp/tearDown，作用于unittest中的测试用例的开始与结束；
    assertEqual(self, first, second, msg=None)，主要通过断言来判断测试用例的执行结果，这种断言，如果第一个参数等于第二个参数，就说明，测试用例执行成功；
    assertTrue(self, expr, msg=None)，只要返回的是True,则断言成功;
    assertIn(self, member, container, msg=None),断言第一个参数是否在第二个参数中(或者说，第二个参数是否包含第一个参数)，有则断言成功，不包含就打印msg；
    assertIs(self, expr1, expr2, msg=None),断言第一个参数和第二个参数是否为同一对象；
    assertIsNone(self, obj, msg=None),断言表达式是否为none对象

'''
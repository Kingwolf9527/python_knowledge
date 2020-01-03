# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/16 5:39

from calculator import Count
import unittest

class TestSub(unittest.TestCase):

    def setUp(self):
        print("test sub start!")

    def test_sub(self):
        j = Count(2, 3)  # 调用计算器的类
        self.assertEqual(j.sub(),5,msg="testcase not pass!")  # 调用减法运算

    def test_sub2(self):
        j = Count(50, 60)
        self.assertEqual(j.sub(),-10,msg="testcase not pass!")

    def tearDown(self):
        print("test sub end!")

if __name__ == '__main__':
    unittest.main()
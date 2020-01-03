# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/16 5:38

from calculator import Count
import unittest

class TestAdd(unittest.TestCase):

    def setUp(self):
        print("test add start!")

    def test_add(self):
        j = Count(2,3)   #调用计算器的类
        self.assertEqual(j.add(),5,msg="testcase not pass!")     #调用加法运算

    def test_add2(self):
        j = Count(50,60)
        self.assertEqual(j.add(),110,msg="testcase not pass!")

    def tearDown(self):
        print("test add end!")

if __name__ == '__main__':
    unittest.main()
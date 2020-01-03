# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/16 5:09

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

    #构建测试集,通过调用unittest.TestSuite()的类来创建测试套件，再通过TestSuite的addTest方法来添加测试用例
    suite = unittest.TestSuite()
    suite.addTest(TestAdd('test_add'))     #添加的测试用例函数是从不同的类里面调用的
    suite.addTest(TestAdd('test_add2'))
    suite.addTest(TestSub('test_sub'))
    suite.addTest(TestSub('test_sub2'))

    #运行测试集合，通过调用unittest.TextTestRunner()类的run()方法来执行测试集合，run(suite),里面的对象是测试的集合
    runner = unittest.TextTestRunner()
    runner.run(suite)


'''
    有一个问题：随着测试用例的激增，如果把所有的测试用例都写在同一个文件中，这个文件会越来越臃肿，后期维护很困难，需要将这些测试用例按照不同的功能进行拆分
    例如把这个文件：分为count一个文件，testadd一个文件，testsub一个文件，runtest一个文件

'''
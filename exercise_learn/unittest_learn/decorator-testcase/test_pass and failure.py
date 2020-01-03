# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/17 1:39

import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    #skip(reason):无条件的跳过装饰的测试，说明跳过测试的原因----------这些方法也可以用在测试类上
    @unittest.skip("直接跳过测试")
    def test_skip(self):
        print("test aaa")

    #skipIf(condition, reason)：跳过装饰的测试，如果条件为真
    @unittest.skipIf(3>5,"当条件为True时，跳过测试")
    def test_skipif(self):
        print("test bbb")

    #skipUnless(condition, reason)：跳过装饰的测试，除非条件为真
    @unittest.skipUnless(3>1,"当条件为True时，执行测试")
    def test_skipunless(self):
        print("test ccc")

    #expectedFailure(test_item)：测试标记为失败，不管执行的结果是否失败，统一标记为失败
    @unittest.expectedFailure
    def test_expect_failure(self):
        self.assertEqual(2,3)

if __name__ == '__main__':
    unittest.main()
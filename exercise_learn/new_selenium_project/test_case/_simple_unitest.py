# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/11/29 3:36

import unittest

class Simple_uni(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print('所有用例的前置条件')
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print('所有用例的后置条件')


    def setUp(self):
        print('01单个用例的前置条件')

    def tearDown(self):
        print('01单个用例的后置条件')

    @unittest.skip('暂时不执行')
    def test_11(self):
        print('11 case')

    def test_02(self):
        self.assertFalse(1>0,'测试case失败，pick')
        print('02 case')

    def test_3(self):
        print('3 case')


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(Simple_uni("test_3"))
    # unittest.TextTestRunner().run(suite)
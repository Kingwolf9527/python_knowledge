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
        print('02单个用例的前置条件')

    def tearDown(self):
        print('02单个用例的后置条件')

    @unittest.skip('暂时不执行')
    def test_111(self):
        print('111 case')

    def test_0222(self):
        print('0222 case')

    def test_33(self):
        self.assertEqual(1,'as','测试failed')
        print('33 case')


if __name__ == '__main__':
    unittest.main()

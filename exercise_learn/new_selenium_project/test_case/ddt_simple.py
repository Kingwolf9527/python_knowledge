# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/12/2 4:13

import unittest
import ddt


data_ = (['2','4'],[2,11],[5,44])

@ddt.ddt
class Test_ddt_simple(unittest.TestCase):

    def setUp(self):
        print('前置条件')

    def tearDown(self):
        print('后置条件')


    @ddt.data(*data_)

    @ddt.unpack
    def test_add(self,a,b):
        print(a+b)



if __name__ == '__main__':
    unittest.main()

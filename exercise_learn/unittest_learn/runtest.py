# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/16 5:40

'''
    这个是常规的通过addTest()方法添加测试用例

'''
# import unittest
#
# #加载测试文件
# import testadd
# import testsub
#
# #构建测试集,通过调用unittest.TestSuite()的类来创建测试套件，再通过TestSuite的addTest方法来添加测试用例
# suite = unittest.TestSuite()
# suite.addTest(testadd.TestAdd('test_add'))     #添加的测试用例函数是从不同的类里面调用的,这里还要从文件.类('函数')
# suite.addTest(testadd.TestAdd('test_add2'))
# suite.addTest(testsub.TestSub('test_sub'))
# suite.addTest(testsub.TestSub('test_sub2'))
#
# if __name__ == '__main__':
#
#     #运行测试集合，通过调用unittest.TextTestRunner()类的run()方法来执行测试集合，run(suite),里面的对象是测试的集合
#     runner = unittest.TextTestRunner()
#     runner.run(suite)

'''
    这样的拆分，带来很多好=好处，可以再细分，根据不同的功能继续完善，但是测试用例的添加还是有很多的问题，因为一旦测试用例的数量很多，不可能通过addTest，一条一条的增删，这个时候，
    unittest.TestLoader(),这个类可以解决这个问题，它是负责根据各种标准加载测试用例的，可以通过它的discover()方法完成：
    discover(self, start_dir, pattern='test*.py', top_level_dir=None):start_dir--要测试的模块或者测试用例的目录 //建议这种方法：case_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),'case') #获取当前目录下的case目录；
                                                                      pattern='test*.py'--表示测试用例文件名的匹配规则，此处以"test"开头的".py"类型的文件，中间的“*”表示任意多个字符
                                                                      top_level_dir--测试模块的顶层目录，如果没有顶层目录，默认为none
'''

'''
    这个是用到unittest.TestLoader().discover()方法，科学找到所以的测试用例文件，不用再一个一个的添加的方法(采用这个默认的加载方法更好：unittest.defaultTestLoader.discover())

'''

import unittest

# #定义测试用例所在的目录
# test_dir = r'F:\local_repository\Spider-learn\new-spider-and-python\new exercise\unittest'
#
# discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
#
# if __name__ == '__main__':
#
#     runner = unittest.TextTestRunner()
#     runner.run(discover)
#
#
# #结果一样，但是过程，大大简化了测试用例的查找于执行

'''
    unittest.defaultTestLoader.discover() + HTMLTestRunner 项目集成测试报告

'''

import unittest
import time
from HTMLTestRunner_PY3 import HTMLTestRunner

#定义测试用例所在的目录
test_dir = r'F:\local_repository\Spider-learn\new-spider-and-python\new exercise\unittest'

#加载测试用例
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ == '__main__':
    #生成按照一定格式的当前时间，拼接到生成的测试报告的文件名中，防止因为没有修改文件名，导致旧数据被覆盖
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")
    file = "F:/HTML_report./" + now_time + "result.html"

    #生成测试报告
    with open(file,'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                verbosity=2,
                                title='测试报告',
                                description='执行人：Kingwolf')
        #run()的对象不再是unittest.TestSuite()，而是unittest.defaultTestLoader.discover()对象
        runner.run(discover)


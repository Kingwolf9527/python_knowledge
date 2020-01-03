# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/18 3:50

import os

#定义测试报告的目录
test_dir = "F:\\HTML_report"

# 利用sort()方法，对目录下的文件以及文件夹按时间重新排序(sort(self, key=None, reverse=False))
# [按key的关键字进行升序排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间，所以最终以文件时间从小到大排序]
# 最后对lists元素，按文件修改时间大小从小到大排序
lists = os.listdir(test_dir)
lists.sort(key=lambda fn:os.path.getmtime(test_dir + '\\' + fn))
print(("最新的文件为：" + lists[-1]))

# 获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
file = os.path.join(test_dir,lists[-1])
print(file)

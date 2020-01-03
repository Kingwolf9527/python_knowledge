# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/8/2 20:54

"""

    两个列表相加，等价于extend

"""

a = [1,2,3]
b = [4,5,6]
c = [8,9]

# d = a + b
# print('列表相加的操作结果是：',d)
#换成list的extend(注意list.extend()是没有返回值的,是从原列表后面添加其他列表的元素进来)
a.extend(b)
print('使用list.extend()添加的结果是：',a)
#结果是：
# [1, 2, 3, 4, 5, 6]
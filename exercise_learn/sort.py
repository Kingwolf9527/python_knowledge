# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/11 2:08

'''
    sort(),reverse()以及sorted()的区别

'''


num1 = [1,5,7,8,10,55,2,77]

#sort()方法:对列表内容进行正向排序，排序后的新列表会覆盖原列表（id不变），也就是sort排序方法是直接修改原列表list排序方法
# num1.sort()
# print(num1)
#结果是：[1, 2, 5, 7, 8, 10, 55, 77]

#reverse()方法:列表反转排序：是把原列表中的元素顺序从左至右的重新存放，而不会对列表中的参数进行排序整理
# num1.reverse()
# print(num1)
#结果是：[77, 2, 55, 10, 8, 7, 5, 1]

#但是简单的赋值可能排序没有效果，要想解决这个问题，就可以用：sorted()和reverse()方法
# n = num1.sort()
# print(n)
# m = num1.reverse()
# print(m)
#结果是：None

#sorted()方法：即可以保留原列表，又能得到已经排序好的列表//sorted()方法可以用在任何数据类型的序列中，返回的总是一个列表形式
k = sorted(num1)
print(sorted(num1))
#结果是：
# [1, 2, 5, 7, 8, 10, 55, 77]



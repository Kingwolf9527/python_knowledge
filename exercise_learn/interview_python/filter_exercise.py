# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/8/2 16:27

"""

    filter方法求出列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表

"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#第一种方法
# def filter_func(x):
#     if x % 2 == 1:
#         return True
#
# new_list = filter(filter_func,a)
# print('filter对象：',new_list)
# new_list = [i for i in new_list]
# print('新列表：',new_list)

#第二种方法
new_list = list(filter(lambda x:x%2==1,a))

print('新列表：',new_list)
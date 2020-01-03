# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/8/2 20:37

"""

    zip()函数在运算时，会以一个或多个序列（可迭代对象）做为参数，返回一个元组的列表。同时将这些序列中并排的元素配对
    zip()参数可以接受任何类型的序列，同时也可以有两个以上的参数;当传入参数的长度不同时，zip能自动以最短序列长度为准进行截取，获得元组

"""

#列表操作(当传入参数的长度不同时，zip能自动以最短序列长度为准进行截取)
a = [1,3]
b = [2,4]
c = [5,7,8,9]

# res1 = [i for i in zip(a,b)]
res1 = [i for i in zip(a,c)]
print('res1的结果是：',res1)
#结果是：
# res1的结果是： [(1, 5), (3, 7)]

#元祖操作
# aa = (1,3)
# bb = (2,4)
#
# res2 = [i for i in zip(aa,bb)]
# print('res2的结果是：',res2)
# #结果是：
# # res2的结果是： [(1, 2), (3, 4)]
#
# #字符串操作(当传入参数的长度不同时，zip能自动以最短序列长度为准进行截取)
aaa = 'abcd'
bbb = 'xyz'

res3 = [i for i in zip(aaa,bbb)]
print('res3的结果是：',res3)
#结果是：
# res3的结果是： [('a', 'x'), ('b', 'y'), ('c', 'z')]
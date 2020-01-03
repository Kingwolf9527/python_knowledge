# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/7/2 17:12

"""

    闭包的延迟特性

"""
# def enclosure():
#
#     a = [lambda x : i * x for i in range(4)]
#     return a
#
# aa = [m(2) for m in enclosure()]
# print(aa)

#结果是：[6,6,6,6]

"""
    加上默认参数，解决延迟特性

"""
# def enclosure():
#
#     a = [lambda x,i=i: i * x for i in range(4)]
#     return a
#
# aa = [m(2) for m in enclosure()]
# print(aa)
#
# #结果是:[0,2,4,6]

"""

    把列表推导式换成嵌套函数

"""
def enclosure(func = []):
    # func = []
    for i in range(4):
        def product(x,i=i):
            a = i * x
            return a
        func.append(product)
    return func

aa = [m(2) for m in enclosure()]
print(aa)


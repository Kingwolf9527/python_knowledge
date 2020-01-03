# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/6/12 1:41


# def set_score(score):
#     def func(val):
#         if val > score:
#             print('pass')
#         else:
#             print('fail')
#     return func
#
# f_100 = set_score(60)
# f_150 = set_score(90)
#
# f_100(88)
# f_150(88)

# #闭包用法
# def decorator(func):
#     def in_func(*args):
#         #元祖的长度不能为空
#         if len(args) == 0:
#             return 0
#         for val in args:
#             #元祖中的数据都应该为整数
#             if not isinstance(val,int):
#                 return 0
#         return func(*args)
#     return in_func
#
# def my_sum(x,y=1):
#
#     return x + y
#
# @decorator
# def my_nn():
#
#     return 777

# dec = decorator(my_sum)
# mm = dec(2)
# print(mm)
# my = my_nn()
# print(my)

装饰器的使用
def decorator(func):
    def in_func(*args,**kwargs):
        print('Arguemnts were: %s,%s' %(args,kwargs))
        return func(*args,**kwargs)
    return in_func

@decorator
def my_sum(x,y=1):

    return x * y

@decorator
def my_foo():

    return 7

mm = my_sum(2,6)
print(mm)

nn = my_foo()
print(nn)
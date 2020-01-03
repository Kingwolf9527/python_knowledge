# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/5/31 6:31

class Decoretor_closure(object):

    def __init__(self,x,y):

        self.x = x
        self.y = y

    #第一种方法
    # def __repr__(self):
    #
    #     return 'Coord:' + str(self.__dict__)

    #更加推荐的方法，第二种方法
    def __str__(self):

        return 'Coord:' + str(self.__dict__)
    #Python 定义了__str__()和__repr__()两种方法，__str__()用于显示给用户，而__repr__()用于显示给开发人员
    __repr__ = __str__


def add(a,b):

    return Decoretor_closure(a.x+b.x,a.y+b.y)

def sub(a,b):

    return Decoretor_closure(a.x-b.x,a.y-b.y)

one = Decoretor_closure(100,200)
two = Decoretor_closure(300,200)
# func = add(one,two)
# #第二种方法直接输出
# print(func)

#第一种方式，需要调用repr()方法，把字符串输出
# print(repr(func))

#结果是:
# Coord:{'y': 400, 'x': 400}

#能够对函数的输入参数和返回值做一些非常有用的检查和格式化工作，将负值的x和 y替换成0。
def wrapper(func):
    def checker(a, b):  # 1
        if a.x < 0 or a.y < 0:
            a = Decoretor_closure(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
        if b.x < 0 or b.y < 0:
            b = Decoretor_closure(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
        ret = func(a, b)
        if ret.x < 0 or ret.y < 0:
            ret = Decoretor_closure(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
        return ret

    return checker

add = wrapper(add)
sub = wrapper(sub)
result = sub(one, two)
print(result)
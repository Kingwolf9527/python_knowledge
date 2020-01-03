# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/8/3 0:03

"""

    fn("one",1）直接将键值对传给字典；
    fn("two",2)因为字典在内存中是可变数据类型，所以指向同一个地址，传了新的额参数后，会相当于给字典增加键值对
    fn("three",3,{})因为传了一个新字典，所以不再是原先默认参数的字典

"""

def func(k,v,dict={}):
    dict[k] = v
    print(dict)

t1 = func("one",1)
t2 = func("teo",2)
t3 = func("three",3,{})   #因为传了一个新字典，所以不再是原先默认参数的字典

#结果是：
# {'one': 1}
# {'one': 1, 'teo': 2}
# {'three': 3}
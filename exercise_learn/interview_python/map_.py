# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/8/2 0:56

import pysnooper

"""

    列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
    map（）函数第一个参数是fun，第二个参数是一般是list，第三个参数可以写list，也可以不写，根据需求

"""
list1 = [1,2,3,4,5]

#第一种方法，直接结合map方法
@pysnooper.snoop('./debug_log.log',prefix='---***---')
def func(x):
    return x ** 2

new_list = map(func,list1)
print('map对象',new_list)
#转为列表
new_list = list(new_list)
print(new_list)

#列表推导式处理
list_2 = [i for i in new_list if i >10]
print(list_2)

#第二种，直接采用列表推导式
# new_list2 = [a**2 for a in list1 if a**2 >10]
# print(new_list2)
# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/7/15 16:40

import copy

a = [1,2,3,['a','b','c']]

b = copy.copy(a)

c = copy.deepcopy(a)

# a.append('小青')
a.insert(0,'小青')

a[4][0] = 'CR7'

print(a)
print(b)
print(c)

#结果是:
# ['小青', 1, 2, 3, ['CR7', 'b', 'c']]
# [1, 2, 3, ['CR7', 'b', 'c']]
# [1, 2, 3, ['a', 'b', 'c']]

#不可变类型，不管是深拷贝还是浅拷贝，地址值和拷贝后的值都是一样的

d = (1,2,3)

e = copy.copy(d)

f = copy.deepcopy(d)

print(id(d))
print(id(e))
print(id(f))

#结果是：
# 2668671205664
# 2668671205664
# 2668671205664

# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/6/12 21:40

a = [1,2,3,4,5]

b = list(map(lambda x:x**2,a))
print(b)

c = [x for x in b if x >10]
print(c)
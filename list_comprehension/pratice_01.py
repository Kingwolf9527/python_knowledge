# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/6/12 3:43


# #第一种场景
# a = ['A','B','C','D']
# b = ['a','b','c','d']

# c = [x+y for x in a for y in b]
# print(c)

##第二种场景
# from itertools import product
# a = ['A','B','C','D']
# b = ['a','b','c','d']
#
# c = list(product(a,b))
# print(c)

#第三种场景
a = [2,2,4,6]
b = [3,3,5,7]

#列表元素相加，乘积
#第一种求和方式
# c = [x+y for x,y in zip(a,b)]
#第二种求和
# c = list(map(lambda x,y:x+y,a,b))

# #第一种求积
# c = [x*y for x,y in zip(a,b)]
#第二种求积
c = list(map(lambda x,y:x*y,a,b))
print(c)


#求和结果是：
# [5, 5, 9, 13]
#求积结果是：
# [6, 6, 20, 42]



#第一种场景结果:
# ['Aa', 'Ab', 'Ac', 'Ad', 'Ba', 'Bb', 'Bc', 'Bd', 'Ca', 'Cb', 'Cc', 'Cd', 'Da', 'Db', 'Dc', 'Dd']

#第二种场景的结果:
# [('A', 'a'), ('A', 'b'), ('A', 'c'), ('A', 'd'), ('B', 'a'), ('B', 'b'), ('B', 'c'), ('B', 'd'), ('C', 'a'), ('C', 'b'), ('C', 'c'), ('C', 'd'), ('D', 'a'), ('D', 'b'), ('D', 'c'), ('D', 'd')]

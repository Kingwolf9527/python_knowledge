# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/8/2 19:08

"""

    x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果

"""
x = "abc"
y = "def"
z = ["d", "e", "f"]

str1 = x.join(y)   #x相当于分隔符
print(str1)
#结果是：
# dabceabcf

str2 = x.join(z)
print(str2)
#结果是：
# dabceabcf

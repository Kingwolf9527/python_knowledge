# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/8/2 20:49

"""
    encode和decode,bytes和str
    a="hello"和b="你好"编码成bytes类型

"""

a = 'hello'
b = '你好'

print('编码前的a类型是：',type(a))
print('编码前的b类型是：',type(b))
#结果是：
# 编码前的a类型是： <class 'str'>
# 编码前的b类型是： <class 'str'>

#编码成bytes类型
c = a.encode('utf-8')
d = b.encode('utf-8')
print('编码后的a类型是：',type(c))
print('编码后的b类型是：',type(d))
#结果是：
# 编码后的a类型是： <class 'bytes'>
# 编码后的b类型是： <class 'bytes'>
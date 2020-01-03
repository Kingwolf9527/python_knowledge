# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/6/12 1:41

score = 60

def func(val):
    print('%s' %id(val))
    if val > score:
        print('pass')
    else:
        print('fail')
    def in_func():
        print(val)
    return in_func

f = func(90)
f()
print(f.__closure__)
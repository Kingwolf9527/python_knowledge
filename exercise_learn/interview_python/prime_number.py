# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/8/11 4:41


"""

    一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等），换句话说就是该数除了1和它本身以外不再有其他的因数。
    (else的另外知识点：我们常见的是if…else…或者if…elif…else诸如此类，但其实for也可以和else搭配出现)

"""
from math import sqrt

#第一种传统方法
def prime_tradition():
    num = int(input('请输入正整数：'))
    if num >1:
        for i in range(2,int(sqrt(num) + 1)):
            if num % i == 0:
                print('输入的数字: %d 不是素数！' %num)
                break
        else:
            print('输入的数字: %d 是素数！' %num)
    else:
        print('输入有误，请重新输入！')
if __name__ == '__main__':
    prime_tradition()

# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/8/6 18:01

import math


"""

    题目1：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
    分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列

"""


# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i != j and i != k and  j != k:
#                 print('最后输出的三位数排列：',(i,j,k))
#结果是：
# 最后输出的三位数排列： (1, 2, 3)
# 最后输出的三位数排列： (1, 2, 4)
# 最后输出的三位数排列： (1, 3, 2)
# 最后输出的三位数排列： (1, 3, 4)
# 最后输出的三位数排列： (1, 4, 2)
# 最后输出的三位数排列： (1, 4, 3)
# 最后输出的三位数排列： (2, 1, 3)
# 最后输出的三位数排列： (2, 1, 4)
# 最后输出的三位数排列： (2, 3, 1)
# 最后输出的三位数排列： (2, 3, 4)
# 最后输出的三位数排列： (2, 4, 1)
# 最后输出的三位数排列： (2, 4, 3)
# 最后输出的三位数排列： (3, 1, 2)
# 最后输出的三位数排列： (3, 1, 4)
# 最后输出的三位数排列： (3, 2, 1)
# 最后输出的三位数排列： (3, 2, 4)
# 最后输出的三位数排列： (3, 4, 1)
# 最后输出的三位数排列： (3, 4, 2)
# 最后输出的三位数排列： (4, 1, 2)
# 最后输出的三位数排列： (4, 1, 3)
# 最后输出的三位数排列： (4, 2, 1)
# 最后输出的三位数排列： (4, 2, 3)
# 最后输出的三位数排列： (4, 3, 1)
# 最后输出的三位数排列： (4, 3, 2)




"""

    题目2：一个整数，它加上100后是一个完全平方数，再加上268又是一个完全平方数，请问该数是多少？
    分析：在10万以内判断，先将该数加上100后再开方，再将该数加上268后再开方，如果开方后的结果满足如下条件，即是结果
    需要单独导进专门处理数学方法的库：math，使用开平方的函数math.sqrt()

"""

# import math
#
# for i in range(100000):
#     #开平方数转为整形
#     a = int(math.sqrt(i+100))
#     b = int(math.sqrt(i+268))
#     if (a * a == i + 100) and (b * b == i + 268):
#         print('输出满足条件的整数是：',i)
#结果是：
# 输出满足条件的整数是： 21
# 输出满足条件的整数是： 261
# 输出满足条件的整数是： 1581





"""

    题目3：输入某年某月某日，判断这一天是这一年的第几天？
    分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于3时需考虑多加一天

"""

# year = int(input("请输入正整数year:\n"))
# month = int(input("请输入正整数month:\n"))
# day = int(input("请输入正整数day:\n"))
#
# month_days = [0,31,59,90,120,151,181,212,243,273,304,334]
#
# if year < 0:
#     print('year error')
#
# if (day < 0) or (day > 31):
#     print('days error')
#
# if 0 < month < 13:
#     sum_days = month_days[month-1]
# else:
#     print('month error')
#
# #总天数=前一个月的总天数(如果是一月份，这里为0)+输入的day
# sum_days += day
#
# #根据sign标志来判断是否是闰年
# sign = 0
# if (year % 400 == 0) or ((year % 4 ==0) and (year % 100 != 0)):
#     sign = 1
# #闰年的2月份有29天，非闰年只有28天
# if (sign == 1) and (month > 2):
#     sum_days += 1
 # print('it is the %dth in this year' %sum_days)




"""

    题目4：输入三个整数x,y,z，请把这三个数由小到大输出。
    分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小


"""
# #把输入的三个整数加入列表中，在排序
# test_list = []
#
# for i in range(3):
#     x = int(input('请输入整数：'))
#     test_list.append(x)
#
# #排序，默认是升序
# test_list.sort()
# print('最终输入的数字的排序是；',test_list)




"""

    题目5：输出9*9口诀。
    分析：分行与列考虑，共9行9列，i控制行，j控制列
    

"""

# for i in range(1,10):
#     for j in range(1,10):
#         result = i * j
#         print('%d * %d = %d' %(i,j,result))
#     print('')

#结果是：
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# 1 * 6 = 6
# 1 * 7 = 7
# 1 * 8 = 8
# 1 * 9 = 9
#
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 4 = 8
# 2 * 5 = 10
# 2 * 6 = 12
# 2 * 7 = 14
# 2 * 8 = 16
# 2 * 9 = 18
#
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12
# 3 * 5 = 15
# 3 * 6 = 18
# 3 * 7 = 21
# 3 * 8 = 24
# 3 * 9 = 27
#
# 4 * 1 = 4
# 4 * 2 = 8
# 4 * 3 = 12
# 4 * 4 = 16
# 4 * 5 = 20
# 4 * 6 = 24
# 4 * 7 = 28
# 4 * 8 = 32
# 4 * 9 = 36
#
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
#
# 6 * 1 = 6
# 6 * 2 = 12
# 6 * 3 = 18
# 6 * 4 = 24
# 6 * 5 = 30
# 6 * 6 = 36
# 6 * 7 = 42
# 6 * 8 = 48
# 6 * 9 = 54
#
# 7 * 1 = 7
# 7 * 2 = 14
# 7 * 3 = 21
# 7 * 4 = 28
# 7 * 5 = 35
# 7 * 6 = 42
# 7 * 7 = 49
# 7 * 8 = 56
# 7 * 9 = 63
#
# 8 * 1 = 8
# 8 * 2 = 16
# 8 * 3 = 24
# 8 * 4 = 32
# 8 * 5 = 40
# 8 * 6 = 48
# 8 * 7 = 56
# 8 * 8 = 64
# 8 * 9 = 72
#
# 9 * 1 = 9
# 9 * 2 = 18
# 9 * 3 = 27
# 9 * 4 = 36
# 9 * 5 = 45
# 9 * 6 = 54
# 9 * 7 = 63
# 9 * 8 = 72
# 9 * 9 = 81





"""

    题目6：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
    分析：　兔子的规律为数列1,1,2,3,5,8,13,21....
    斐波那契数列处理

"""

#第一种方法，使用递归方法(写法最简洁，但是效率最低，会出现大量的重复计算，时间复杂度O（1.618^n）,而且最深度1000)
# def fib(n):
#     if n < 0:
#         print('data error')
#     elif n == 0 or n == 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
#
# rabbit_num = fib(40)
# print(rabbit_num)

#第二种 递推法(递推法，就是递增法，时间复杂度是 O(n)，呈线性增长，如果数据量巨大，速度会越拖越慢)
# def fib(n):
#     a,b = 0,1
#     for i in range(n+1):
#         a,b = b,a+b
#     return a
#
# for j in range(40):
#     print('rabbit number is：',fib(j))

#第三种 生成器
# def fib(max_time):
#     a,b = 0,1
#     while max_time > 0:
#         a,b = b,a+b
#         max_time -= 1
#         yield a
#
# for i in fib(40):
#     print('rabbit number is:',i)





"""

    题目7：判断101-200之间有多少个素数，并输出所有素数。
    分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数
    
    判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数

"""
#第一种方法，常规的
# l = []
# for x in range(20):
#     if x < 2:
#         continue
#     for i in range(2,int(math.sqrt(x)+1)):
#         if x % i == 0:
#             break
#     else:
#         l.append(x)
#
# print('素数的个数是：',len(l))
# print(l)

#第二种，输入随机数，判断素数

# input_num = int(input("任意输入一个数字："))
#
# if input_num > 1:
#     for i in range(2, int(math.sqrt(input_num) + 1)):
#         if input_num % i == 0:
#             print('输入的该数字%d 不是素数！' %input_num)
#             break
#     else:
#         print('输入的该数字：%d 是素数' % input_num)
# else:
#     print('输入的数字不合法，请输入大于1的数字')


#1
# #第二种方法，改进版
#
# def add_odd():
#     """
#     生成一个奇数生成器
#     :return:
#     """
#     n = 1
#     while True:
#         n += 2
#         yield n
#
# def judge_prime(n):
#     """
#     过滤掉n的倍数的数
#     :param n:
#     :return:
#     """
#     is_prime = lambda x:x % n > 0
#     return is_prime
#
# def prime():
#     """
#     获取当前序列的第一个元素，然后删除后面序列该元素倍数的数，然后构造新序列
#     :return:
#     """
#     yield 2
#     #初始化序列
#     it = add_odd()
#     while True:
#         #返回序列的第一个元素
#         n = next(it)
#         print(n)
#         yield n
#         it = filter(judge_prime(n),it)
#
# if __name__ == '__main__':
#     for n in prime():
#         if n < 10000:
#             print(n)
#         else:
#             break





"""

    题目8：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。
    分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位


"""

# number_list = []
# for n in range(100,1000):
#     #百位数字
#     i = int(n / 100)
#     #十位数字
#     j = int(n / 10) % 10
#     #个位数字
#     k = n % 10
#     if n == i ** 3 + j ** 3 + k ** 3:
#         number_list.append(n)
# print('水仙花数字的个数：%d' %(len(number_list)))
# print('水仙花数字列表是：',number_list)




"""

    题目9：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
    分析：利用while语句,条件为输入的字符不为'\n'.


"""

#
# s = input('Input String:\n')
# #初始化计数
# letters = 0
# space = 0
# digit = 0
# other = 0
#
# for x in s:
#     if x.isalpha():
#         letters += 1
#     elif x.isspace():
#         space += 1
#     elif x.isdigit():
#         digit += 1
#     else:
#         other += 1
#
# print('输入的字符中，字母的个数：%d' % letters)
# print('输入的字符中，空格的个数：%d' % space)
# print('输入的字符中，数字的个数：%d' % digit)
# print('输入的字符中，其他字符的个数：%d' % other)




"""

    题目10：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？


"""
# import pysnooper
#
# high = 100
# sum_meter = 0
#
# @pysnooper.snoop(output='./test.log',prefix='---***---')
# def height():
#     for i in range(10):
#         global sum_meter
#         global high
#         if i == 0:
#             sum_meter += high
#             high /= 2
#
#         else:
#             sum_meter += (2*high)
#             high /= 2
#     print('-------------------------------')
#     print('第十次落地可以反弹的高度为：%f米' %(high))
#     print('一共经过了%f米' %(sum_meter))
#
# if __name__ == '__main__':
#     h = height()





"""

    题目11：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
    分析：请抓住分子与分母的变化规律
    符合斐波那契数列

"""

def fib(max_time):
    m = 2.0
    d = 1.0
    s = 0
    while max_time > 0:
        s += m / d
        m,d = m+d,m
        max_time -= 1
        yield s
for i in fib(20):
    print(i)





"""

    题目12：求1+2!+3!+...+20!的和
    分析：此程序只是把累加变成了累乘


"""

# #初始化总和和第一个数
# s = 0
# t = 1
#
# for n in range(1,21):
#     t *= n
#     s += t
#     print('累加的和是： %d' %s)




"""

    题目13：利用递归方法求5!。
    分析：递归公式：fn=fn_1*4!

"""
#
# def fact(i):
#     sum_ = 0
#     if i == 0:
#         sum_ = 1
#     else:
#         sum_ = i * fact(i-1)
#         print(sum_)
#     return sum_
#
# if __name__ == '__main__':
#     f = fact(5)





"""


    题目14：有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
    分析：利用递归的方法，递归分为回推和递推两个阶段。要想知道第五个人岁数，需知道第四人的岁数，依次类推，推到第一人（10岁），再往回推


"""

# def age(n):
#     if n == 1:
#         p_age = 10
#     else:
#         p_age = age(n-1) + 2
#         print('每个人的年龄是： %d' %p_age)
#     return p_age
#
# if __name__ == '__main__':
#     a = age(5)





"""

    题目15：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n(利用指针函数)


"""

# def odd(n):
#     a = 1
#     s = 1
#     while True:
#         s += a / n
#         print(s)
#         return s
#
# def even(n):
#     a = 1
#     s = 0
#     while True:
#         s += a / n
#         print(s)
#         return s
#
# def func():
#     n = int(input('输入一个整数：\n'))
#     if n == 0:
#         print('请输入非零的正整数！')
#     elif n % 2 == 0:
#         print('输入的整数是偶数，调用偶数方法！')
#         even(n)
#     else:
#         print('输入的整数是奇数，调用奇数方法！')
#         odd(n)
#
# if __name__ == '__main__':
#     f = func()






"""

    题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件“test”中保存。
　　　输入的字符串以！结束

"""


# with open('test.txt','w',encoding='utf-8') as f:
#     str_word = input('输入小写字母：\n')
#     str_word = str_word.upper()
#     f.write(str_word)

# with open('test.txt','r',encoding='utf-8') as f:
#     s = f.read()
#     print(s)






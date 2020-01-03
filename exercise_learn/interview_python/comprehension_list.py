# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/8/2 18:21

"""

    列表推导式：
    [[1,2,7],[3,4,8],[5,6,9]]一行代码展开该列表，得出[1,2,3,4,5,6,7,8,9]以及[1,3,5]以及[1,4,9]

"""


a = [[1,2,7],[3,4,8],[5,6,9]]

#1-1得到最终结果：[1,2,3,4,5,6,7,8,9]---------常规方法
# new_list1 = []
# for i in a:
#     for j in i:
#         new_list1.append(j)

#1-2-------列表推导式处理
new_list1 = [i for res in a for i in res]

print('new_list1的结果是：',new_list1)
#结果是：
# new_list1的结果是： [1, 2, 7, 3, 4, 8, 5, 6, 9]

#2-1得到的结果是：[1,3,5]-----------常规方法
# new_list2 = []
# for i in range(len(a)):
#     ret = a[i][0]
#     new_list2.append(ret)

#2-2列表推导式处理
new_list2 = [a[i][0] for i in range(len(a))]

print('new_list2的结果是：',new_list2)
#结果是：
# new_list2的结果是： [1, 3, 5]

#3-1得到的结果是：[1,4,9]-----------常规方法
# new_list3 = []
# for i in range(len(a)):
#     ret = a[i][i]
#     new_list3.append(ret)

#3-2列表推导式处理
new_list3 = [a[i][i] for i in range(len(a))]

print('new_list3的结果是：',new_list3)
#结果是：
# new_list3的结果是： [1, 4, 9]


""""

    更骚气处理：用numpy矩阵处理，把列表转为矩阵

"""

import numpy as np

b =np.array(a).flatten().tolist()
print('numpy处理的结果是：',b)
#结果是：
# numpy处理的结果是： [1, 2, 7, 3, 4, 8, 5, 6, 9]

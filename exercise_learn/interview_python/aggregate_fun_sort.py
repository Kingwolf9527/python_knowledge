#- * - coding:utf-8
#__author__ : kingwolf
#createtime : 2019/12/31 17:56

"""

    a=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
    使用聚合函数，min()方法处理

"""

a=[2,3,5,4,9,6]
# 存储最小值的列表
new_list = []

def sort_list(a):

    # 返回列表中最小的值
    b = min(a)

    # 每次存储最小的元素
    new_list.append(b)

    # 原列表删除最小的元素
    a.remove(b)

    if len(a) > 0:
        sort_list(a)
    return new_list


tt = sort_list(a)
print(tt)
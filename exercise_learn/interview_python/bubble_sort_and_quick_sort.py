#- * - coding:utf-8
#__author__ : kingwolf
#createtime : 2020/1/10 2:50


"""

    冒泡排序以及快速排序

    冒泡排序：相邻两个元素比较，大的排后面，第一次把最大的数排在最后一位；
    冒泡排序总共排的次数为：1+2+3+…+n-1,共 n(n-1)/2，时间复杂度为n平方；

    快速排序：选取数组的某一个数作为基准（一般选第一个最后一位）， 排列整个数值，比基准小的排到左边，比基准大的数 排在右边
    继续选取新生成的数值的第一个数 进行排序； 时间复杂度为nlogn

"""

import time
import pysnooper


#冒泡排序
# @pysnooper.snoop(output='./bubbleSort.log',prefix='=+=')
# def bubbleSort(testList):
#     #排序的次数
#     for i in range(len(testList)-1):
#         #元素的下标
#         for j in range(len(testList)-1-i):
#             #数据交换
#             if testList[j] > testList[j+1]:
#                 testList[j],testList[j+1] = testList[j+1],testList[j]
#
#     return testList
#
# testList = [10,2,120,0,-20,55]
# testResult = bubbleSort(testList)
# print(testResult)


#冒泡排序优化
# @pysnooper.snoop(output='./bubbleSort2.log',prefix='===')
# def bubbleSort(testList):
#
#     #排序的次数
#     for i in range(len(testList)-1):
#         # 用来标志数据是否发生改变(因为如果冒泡排序执行了一趟而没有交换发生，说明该列表已经是有序状态，可以直接结束算法)
#         numberChange = False
#         #元素的下标
#         for j in range(len(testList)-1-i):
#             #数据交换
#             if testList[j] > testList[j+1]:
#                 testList[j],testList[j+1] = testList[j+1],testList[j]
#                 numberChange = True
#
#         if not numberChange:
#             return testList
#
#     return testList
#
# testList = [10,2,120,0,-20,55]
# testResult = bubbleSort(testList)
# print(testResult)
#测试结果是：
# [-20, 0, 2, 10, 55, 120]




#快速排列
@pysnooper.snoop(output='./quickSort.log',prefix='--**--')
def quickSort(testList):

    #判断基线条件
    if len(testList) < 2:
        return testList
    else:
        #设置基准值
        baseValue = testList[0]
        #小于基准值的数列
        lessList = [i for i in testList if i < baseValue]
        #等于基准值的数列
        equalList = [i for i in testList if i == baseValue]
        #大于基准值的数列
        greaterList = [i for i in testList if i > baseValue]

        #返回排列好的数列(内部需要再次排序处理)
        return  quickSort(lessList) + equalList + quickSort(greaterList)



testList = [10,2,120,0,-20,55]
testResult = quickSort(testList)
print(testResult)
## 测试结果:
#[-20,0,2,10,55,120]

# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/11 1:21

'''
    Python实现：冒泡排序

'''

def bubblesort(nums):
    for i in range(len(nums)-1):          # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums)-1-i):    # ｊ为列表下标
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums


nums = [1,10,5,59,100,2,3,77]
bs = bubblesort(nums)
print(bs)

#结果
# [1, 2, 3, 5, 10, 59, 77, 100]

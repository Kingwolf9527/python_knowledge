# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/8/2 1:33


"""

    去重并从小到大排序输出"adfjl"
    set去重，去重转成list,利用sort方法排序，reeverse=False是从小到大排
    list是不变数据类型

"""
# s = "ajldjlajfdljfddd"
# #去重
# set1 = set(s)
# #转为列表,排序前
# list1 = list(set1)
# print(list1)
#
# #排序方法一，没有返回值的
# # list1.sort(reverse=False)
# # print(list1)
#
# #排序方法二，有返回值的
# list2 = sorted(list1,reverse=False)
# print(list2)
#
# #列表转为字符串输出
# res = ''.join(list2)
# print(res)

#结果是：
# ['f', 'd', 'a', 'l', 'j']
# ['a', 'd', 'f', 'j', 'l']
# adfjl


"""

    字典根据键从小到大排序

"""

# dict1 = {"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
#
# list3 = sorted(dict1.items(),key=lambda i:i[0],reverse=False)
# print('sorted根据字典键排序是：',list3)
# #常规方式
# # new_dict = {}
# # for i in range(len(list3)):
# #     new_dict[list3[i][0]] = list3[i][1]
#
# #采用字典推导式处理
# new_dict = {i[0]:i[1] for i in list3}
# print('新字典是：',new_dict)

#结果是：
# sorted根据字典键排序是： [('age', 18), ('city', '深圳'), ('name', 'zs'), ('tel', '1362626627')]
# 新字典是： {'age': 18, 'city': '深圳', 'name': 'zs', 'tel': '1362626627'}



"""
    操作方法:利用min()方法求出最小值，原列表删除最小值，新列表加入最小值，递归调用获取最小值的函数，反复操作
    list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]

"""

# List_1 = [2,3,5,4,9,6]
#
# #存储最小值的排序列表
# new_list = []
#
# def get_list(List):
#     #获取列表的最小值
#     min_element = min(List)
#     #原列表删除最小元素
#     List.remove(min_element)
#     #将最小值添加到新列表中
#     new_list.append(min_element)
#
#     #保证最后列里面有值，递归调用取值(因为每次取值都会删除最小元素)
#     if len(List) > 0:
#         get_list(List)
#     return new_list
#
# if __name__ == '__main__':
#     list_test = get_list(List_1)
#     print(list_test)
#     #结果是：
#     # [2, 3, 4, 5, 6, 9]



"""

    使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为
    [0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小
    先按照正负排先后，再按照大小排先后       （布尔值比较：false < true）

"""

# a = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
#
# #方法一
# #先按照正负排先后，再按照大小排先后(FALSE<TRUE)
# b = sorted(a,key=lambda x:(x<0,abs(x)))
# print('排序完成后，完整的列表是：',b)
#结果是：
# 排序完成后，完整的列表是： [0, 2, 4, 8, 8, 9, -2, -4, -4, -5, -20]

#方法二
#其他方法，结合filter方法

# aa = list(filter(lambda x:x>=0,a))
# aa.sort(reverse=False)
#
# bb = list(filter(lambda x:x<0,a))
# bb.sort(reverse=True)
#
# #组合最终列表
# aa.extend(bb)
# print(aa)






"""

    列表嵌套列表排序，年龄数字相同怎么办(多重元祖比较，先比较第一个值，如果相同，在比较第二个值，以此类推)

"""

# g = [['zs',19],['ll',54],['wa',23],['df',23],['xf',23]]

#按照字母排序
h = sorted(g,key=lambda x:x[0],reverse=False)
print('按照字母排序的结果是：',h)
#结果是：
# 按照字母排序的结果是： [['df', 23], ['ll', 54], ['wa', 23], ['xf', 23], ['zs', 19]]


#按照年龄进行排序(年龄有相同，比较其他项，在这里是比较前面的字母)
j = sorted(g,key=lambda x:(x[1],x[0]))
print('按照年龄的排序结果是：',j)
#结果是：
# 按照年龄的排序结果是： [['zs', 19], ['df', 23], ['wa', 23], ['xf', 23], ['ll', 54]]



"""

    根据字符串长度排序

"""

# k = ['ac','n','dlk','juhg','ytrew']
# #按照字符串长度排序
# l = sorted(k,key=lambda x:len(x),reverse=False)
# print('字符串长度的排序是：',l)
#结果是：
# 字符串长度的排序是： ['n', 'ac', 'dlk', 'juhg', 'ytrew']

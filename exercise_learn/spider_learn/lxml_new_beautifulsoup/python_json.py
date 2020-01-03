# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/26 22:23

import json

#将Python对象转为json字符串

# persons = [
#
#     {
#         'username':'狼胸',
#         'age':18
#
#     },
#
#     {
#         'username':'我罗',
#         'age':20
#
#     }
# ]
# #第一种存储方式
# # json_str = json.dumps(persons)
# # with open('person_test.json','w') as f:
# #     f.write(json_str)
# # print(type(json_str))
# # print(json_str)
# #结果是：
# # <class 'str'>
# # [{"age": 18, "username": "king"}, {"age": 20, "username": "wolf"}]   单引号自动转为双引号了
#
# #第二种存储方式:保存的数据有中文的时候，写文件进去的时候，先指定编码方式，而且ensure_ascii需要设置为False，默认是true的
# with open('persons_test2.json','w',encoding='utf-8') as f:
#     json.dump(persons,f,ensure_ascii=False)


#将json字符串loads成Python对象
# json_str = '[{"username": "狼胸", "age": 18}, {"username": "w我罗", "age": 20}]'
#
# persons = json.loads(json_str)
# print(type(persons))
# print(persons)
# #结果是：
# # <class 'list'>
# # [{'age': 18, 'username': '狼胸'}, {'age': 20, 'username': 'w我罗'}]

#用读取文件的方式，将json字符串loads成Python对象
with open('persons_test2.json','r',encoding='utf-8') as f:
    persons= json.load(f)
    print(type(persons))
    for person in persons:
        print(person)
# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/13 1:38

"""

    列表中，出现次数最多的前4个数字
    第一种方法：用已经封装好的collections库的Counter方法
    第二种方法：常规方法


"""

from collections import Counter

# words = [
#     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
#     'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
#     'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
#     'my', 'eyes', "you're", 'under'
# ]

# word_counts = Counter(words)
#
# #所有单词出现的次数
# all_conut_words = word_counts
# # print(all_conut_words)
# #结果是：
# # Counter({'eyes': 8, 'the': 5, 'look': 4, 'my': 3, 'into': 3, 'around': 2, 'under': 1, "you're": 1, "don't": 1, 'not': 1})
#
# #出现次数最多的单词
# max_count_word = word_counts.most_common(1)
# # print(max_count_word)
# #结果是：
# # [('eyes', 8)]
#
# #出现次数最多的前4个单词是：
# other_max_count_word = word_counts.most_common(4)
# print(other_max_count_word)
#结果是：
# [('eyes', 8), ('the', 5), ('look', 4), ('my', 3)]


#    第二种方法：常规方法
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

nunber_dict_count = {}

for i in words:
    if i not in nunber_dict_count:
        nunber_dict_count[i] = 1
    else:
        nunber_dict_count[i] += 1

#从多到少排序处理，降序
nunber_dict_list = sorted(nunber_dict_count.items(),key=lambda x:(x[1],x[0]),reverse=True)
print(nunber_dict_list[:])


"""

    利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"，输出出现次数前四的

"""
# from collections import Counter
#
# str_ = 'kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h'
#
# count_times = Counter(str_)
# #打印所有字母出现的次数
# print(count_times)
#
# #打印出现次数前4的字母
# most_count_four = count_times.most_common(4)
# print(most_count_four)

#结果是：
# Counter({'l': 9, 'h': 6, ';': 6, 'f': 5, 'a': 4, 'j': 3, 'd': 3, 's': 2, 'b': 1, 'k': 1, 'g': 1})
# [('l', 9), ('h', 6), (';', 6), ('f', 5)]

#第二种方法：
# str_ = 'kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h'
#
# nunber_dict_count = {}
#
# for i in str_:
#     if i not in nunber_dict_count:
#         nunber_dict_count[i] = 1
#     else:
#         nunber_dict_count[i] += 1
#
# #从多到少排序处理，降序
# nunber_dict_list = sorted(nunber_dict_count.items(),key=lambda x:(x[1],x[0]),reverse=True)
# print(nunber_dict_list[:4])
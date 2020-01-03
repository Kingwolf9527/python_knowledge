# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/8/30 5:14


#magic函数分两种：一种是面向行的，另一种是面向单元型的:1-行magic函数是用前缀“%”标注的，很像我们在系统中使用命令行时的形式，例如在Mac中就是你的用户名后面跟着“$”。“%”后面就是magic函数的参数了，但是它的参数是没有被写在括号或者引号中来传值的
#2-

import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 中文乱码的处理,设置全局字体，以支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决‘-’表现为方块的问题
plt.rcParams['axes.unicode_minus'] = False

#读取链家网房源数据的csv文件
lj = pd.read_csv('F:\lianjia1.csv',encoding='gbk')
#删除不需要的列，比如这里的href(链接)，这里不需要
del lj['href']
# print(lj.head())
# print(lj.info())  #查看数据中各个字段的相关信息，总数据，还有数据类型

#按照行政区域分组，再对单价进行平均
mean_value = lj.groupby('region')

'''
    第一步：各区域的单价的均值
'''
# #画图
# fig = plt.figure(figsize=(12,7))    #figsize=(12,7)指定图片的大小
# #Axes实例
# ax = fig.add_subplot(111)    #Axes实例：111,第一个1代表子图的总行数，第二个1代表子图的总列数，第三个1代表子图的位置
# #设置顶部标题
# ax.set_title('广州各区域二手房的均价')
#
# # 绘图（取均值的方法：mean()）--对单价进行平均  //plt.plot :设置色彩和样式   bar()是柱状
# mean_value['unit_price'].mean().plot.bar()
# # mean_value.unit_price.mean().plot.bar()
#
# #保存图片
# plt.savefig('per_price.jpg')
# s = plt.show()
# print(s)

'''
    第二步：各区域房间面积的均值

'''
# #对area进行一些设置，因为数据库的area是XX平米的，在图形上展示(y轴)，需要把平米替换为空----利用apply()函数中的lambda表达式处理,有替换功能
# lj['area'] = lj['area'].apply(lambda x: x.replace('平米',''))
# #设置数据类型（常用：numpy.dtype()-查看数据类型    //numpy.astype()-设置/改变数据类型），设置为浮点数
# #numpy中的数据类型转换，不能直接改原数据的dtype!  只能用函数astype()
# lj['area'] = lj['area'].astype(np.float)
#
# #画图
# fig2 = plt.figure(figsize=(12,7))
# #Axes实例
# ax2 = fig2.add_subplot(111)
# #设置顶部标题
# ax2.set_title('广州各区域二手房的面积均值')
# # 绘图
# mean_value['area'].mean().plot.bar()
# #保存图片
# plt.savefig('per_area.jpg')
# s2 = plt.show()
# print(s2)

'''
    第三部：房屋的建造时间分别情况

'''

#先要对数据进行格式转换，将对象格式转换成数值类型，再使用正则表达式，将房屋价格中的数字保留下来，将其余的汉字删除掉，最后只是取其中出现次数最多的前20个进行画图

# #正则匹配，去掉汉字，保留数据
# def number(x):
#     a = re.findall('\d+',x)
#     if len(a) == 0:
#         return None
#     else:
#         return a[0]
# lj['build_year'] = lj['build_year'].apply(number)
#
# #画饼状图
# fig3 = plt.figure(figsize=(8,8))
# #Axes实例
# ax3 = fig3.add_subplot(111)
# #设置顶部标题
# ax3.set_title('广州地区二手房的建造时间分布')
#
# # 绘图(柱状的是.bar(),饼状的是.pie()) //取其中出现次数最多的前20个(也就是取值出现最高的前20个,用pandas.value_counts()--其值为频率)
# #并且设置图形的色彩为rainbow
# lj['build_year'].value_counts()[:20].plot.pie(cmap=plt.cm.rainbow,autopct='%.2f')
# #cmap的值是颜色图谱(colormap)的值，cmap = plt.cm.图谱
# # 颜色图谱                          描述
# # autumn                        红-橙-黄
# # bone                          黑-白，x线
# # cool                          青-洋红
# # copper                         黑-铜
# # flag                           红-白-蓝-黑
# # gray                              黑-白
# # hot                            黑-红-黄-白
# # hsv                hsv颜色空间， 红-黄-绿-青-蓝-洋红-红
# # inferno                     黑-红-黄
# # jet                             蓝-青-黄-红
# # magma                      黑-红-白
# # pink                               黑-粉-白
# # plasma                       绿-红-黄
# # prism                         红-黄-绿-蓝-紫-...-绿模式
# # spring                             洋红-黄
# # summer                             绿-黄
# # viridis                             蓝-绿-黄
# # winter                             蓝-绿
#
# #保存图片
# plt.savefig('build_year2.jpg')
# s3 = plt.show()
# print(s3)

'''
    第四步：把上面的建造时间变为直方图显示

'''
# #pandas.DataFrame.fillna()函数是用来填充缺失数据的，里面的参数：inplace设置为True，意味着在原DataFrame中修改，默认是False的
# #因为，画直方图，在一定的范围内，有一些值是没有数据的，需要填充，所以用到fillna()函数，直接改原来的DataFrame,这里用中位数去取值(中位数：median())
# #中位数是通过排序得到的，它不受最大、最小两个极端数值的影响,部分数据的变动对中位数没有影响，当一组数据中的个别数据变动较大时，常用它来描述这组数据的集中趋势
# #数据填充
# lj['build_year'].fillna(lj['build_year'].median(),inplace=True)
# #数据类型转换
# lj['build_year'] = lj['build_year'].astype(np.int)
# #画直方图
# fig4 = plt.figure(figsize=(12,7))
# #Axes实例
# ax4 = fig4.add_subplot(111)
# #设置顶部标题
# ax4.set_title('广州地区二手房的建造时间分布直方图')
# # 绘图(直方图的绘制：hist()--里面的重要参数：bins: 直方图的柱数，可选项，默认为10)
# lj['build_year'].plot.hist(bins=12)
# #设置x轴的范围
# plt.xlim((1993,2020))
# #保存图片
# plt.savefig('build_year_hist2.jpg')
# s4 = plt.show()
# print(s4)

'''
    第五步：分析房屋的结构类型，比如是楼板房还是平房这样的信息

'''
#使用正则表达式将数字等信息删除，保留楼板房还是平房这样的信息,用re.sub()，把所有数字都替换为空
# def sub_build(x):
#     b = re.sub('\d+','',x)
#     #再把"建"，"年"，"暂无数据"这些也要处理掉，只保留塔楼，平方之类的描述,用str.replace()处理就行了,可以不断的替换--str.replace().replace()
#     c = b.replace('建','').replace('年','').replace('暂无数据','无')
#     return c
# lj['build_type'] = lj['build_year'].apply(sub_build)
# #因为存在暂无数据，所以要剔除这部分的数据,从value_counts()的频率中把它删除---build_type为建造类型的频率或者出现的次数
# build_type = lj['build_type'].value_counts()
# del build_type['无']
# #画饼状图
# fig5 = plt.figure(figsize=(8,8))
# #Axes实例
# ax5 = fig5.add_subplot(111)
# #设置顶部标题
# ax5.set_title('广州二手房的结构类型')
# # 绘图--cmap=plt.cm.rainbow：是设置色彩，autopct='%2.f':是显示百分百，保留小数点两位
# build_type.plot.pie(cmap=plt.cm.rainbow,autopct='%.2f')
# #保存图片
# plt.savefig('build_type3.jpg')
# s5 = plt.show()
# print(s5)

'''
    第六步：装修情况

'''
# def strip(x):
#     return x.strip()
#
# # lj['decoration'] = lj['decoration'].apply(strip)
# # #设置为唯一,unique()函数-类似set()，取唯一的值，例如：(1,1,1,2,3,3,3,3,3),用了unique（），结果就是(1,2,3)
# lj['decoration'].unique()
# #因为存在'其他'这种数据 ，所以要剔除这部分的数据,从value_counts()的频率中把它删除---decoration为装修情况的频率或者出现的次数
# decoration = lj['decoration'].value_counts()
# #两种方式：lj.decoration以及lj['decoration']
# # lj.decoration = lj.decoration.apply(strip)
# # lj.decoration.unique()
# # decoration = lj.decoration.value_counts()

# del decoration['其他']

# #画饼状图
# fig6 = plt.figure(figsize=(10,6))
# #Axes实例
# ax6 = fig6.add_subplot(111)
# #设置顶部标题
# ax6.set_title('广州二手房的装修情况')
# # 绘图
# decoration.plot.bar()
# #保存图片
# plt.savefig('decoration2.jpg')
# s6 = plt.show()
# print(s6)

'''
    第七步：街区的均价前十

'''
# #数据类型转化
# lj.unit_price = lj.unit_price.astype(np.int)
# #排序，对单价的前十进行排序  //DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')  --by:拿哪个数据来排序(by='') --ascending:排序的类型，如果为true是升序，false是降序  --inplace：根据布尔类型决定是否修改原文件
# new_per_price = lj.sort_values(by='unit_price',ascending=False)[:10]
# #设置单索引和复合索引:set_index() --DataFrame.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False) //append添加新索引，drop为False，inplace为True时，索引将会还原为列
# new_per_price.set_index(new_per_price.name,inplace=True)
#
# #处理一下面积的数据
# def clean_area(x):
#     return x.replace('平米','')
# new_per_price.area = new_per_price.area.apply(clean_area)
# new_per_price.area = new_per_price.area.astype(np.float)
#
# #转化
# area_price = new_per_price.unit_price
# #画图
# fig7 = plt.figure(figsize=(12,7))
# #Axes实例
# ax7 = fig7.add_subplot(111)
# #设置顶部标题
# ax7.set_title('单价最高Top10')
# # 绘图
# area_price.plot.bar()
# #保存图片
# plt.savefig('area_price2.jpg')
# s7 = plt.show()
# print(s7)

'''
    第八步：房屋整体结构的占比情况

'''
#两种索引方式其实都是可以的：'.'和'['']'
#如果不存在函数与dataframe数据的列名相同，两种索引方式都是可以的

# #处理数据
# lj['style'].unique()  #因为存在一个style的函数，如果用lj.style它就不是dataframe了(也不是索引的意思，!=lj['style'])，无法用到value_counts()这个函数
# style2 = lj['style'].value_counts()[:6]
# #画图
# fig8 = plt.figure(figsize=(8,8))
# #Axes实例
# ax8 = fig8.add_subplot(111)
# #设置顶部标题
# ax8.set_title('房屋整体结构占比情况')
# # 绘图,把频率出现最多的前6种结构显示出来
# # lj['style'].value_counts()[:6].plot.pie(cmap=plt.cm.rainbow,autopct='%.2f')
# style2.plot.pie(cmap=plt.cm.rainbow,autopct='%.2f')
# #保存图片
# plt.savefig('style3.jpg')
# s8 = plt.show()
# print(s8)

'''
    第九步：房源朝向分布情况

'''
#处理一下"暂无数据"的数据
def orientation_strip(x):
    return x.strip()
lj.orientation = lj.orientation.apply(orientation_strip)
lj.orientation.unique()
orientation = lj.orientation.value_counts()
del orientation['暂无数据']
#画图
fig9 = plt.figure(figsize=(12,7))
#Axes实例
ax9 = fig9.add_subplot(111)
#设置顶部标题
ax9.set_title('房源朝向分布情况')
# 绘图,把频率出现最多的前10种结构显示出来
orientation[:10].plot.bar()
#保存图片
plt.savefig('orientation2.jpg')
s9 = plt.show()
print(s9)
# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/2/23 3:37

"""

    xlrd:读取excel的一个实例学习

"""

import xlrd

ex = xlrd.open_workbook('user_info.xlsx')   #打开excel

table = ex.sheets()[0]       #通过索引获取工作表，也可以通过其他方式
# table = ex.sheet_by_index(0)
# table = ex.sheet_by_name('account_info')

row = table.row_values(0)      #获取第一行内容
col = table.col_values(0)       #获取第一列内容

rows = table.nrows          #获取所有行数
cols = table.ncols          #获取所有列数

cel_value = table.cell(0,0).value      #获取单元格的值，下面两种方法都可以
cel_value2 = table.cell_value(3,1)
print(cel_value2)
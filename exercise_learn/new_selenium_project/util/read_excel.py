# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/12/3 6:39

import xlrd
import os
from xlutils.copy import copy


class Read_Excel(object):

    def __init__(self,filepath=None,index=None):

        if filepath == None:
            filepath_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'data')
            self.filepath = os.path.join(filepath_dir,'register_data_test.xls')
        else:
            self.filepath = filepath

        if index == None:
            index = 0
        else:
            index = index

        #打开excel文件(设置formatting_info，让excel表格的样式保持原来的)
        self.data = xlrd.open_workbook(self.filepath,formatting_info=True)

        #获取excel的sheet
        self.table = self.data.sheets()[index]


    def processing_data(self):

        #存储每一行的数据
        result = []

        #容错处理，总行数不为空才执行循环
        rows = self.get_nrows()
        if rows != False:
            for i in range(rows):
                #处理每一行的数据，把可能出现的浮点型数据转化为字符串(每一行数据都是一个列表)
                row_data = [self.change_float_data(value) for value in self.table.row_values(i)]
                if row_data:
                    result.append(row_data)

        return result

    def change_float_data(self,value):
        """
        处理浮点数
        :param value:
        :return:
        """
        if isinstance(value,float):
            value = str(int(value))
        return value

    def get_nrows(self):
        """
        获取excel的总行数
        :return:
        """
        rows = self.table.nrows
        #总行数大于等于1才，返回值，提前做处理
        if rows >=1:
            return rows
        return None

    def get_ncols(self):
        """
        获取excel的总列数
        :return:
        """
        cols = self.table.ncols
        #总列数大于等于1才，返回值，提前做处理
        if cols >=1:
            return cols
        return None

    def get_cell_value(self,row,col):
        """
        获取单元格数据
        :param row: 行号
        :param col: 列号
        :return:
        """
        #输入的行号需要小于等于总行数或者总列数
        if self.get_nrows() > row:
            cell_data = self.table.cell_value(row,col)
            return cell_data
        return None

    def write_value(self,row,col,value):
        """
        写入数据
        :param row:
        :param col:
        :return:
        """
        #先复制数据
        read_value = xlrd.open_workbook(self.filepath,formatting_info=True)
        copy_data = copy(read_value)

        #写入数据
        write_data = copy_data.get_sheet(0)
        write_data.write(row,col,value)

        #保存数据
        write_data.save(self.filepath)




if __name__ == '__main__':

    ex = Read_Excel()
    data_ = ex.processing_data()
    print(data_)


# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/2/23 5:28

import xlrd
import os


class Xlsx_Excel(object):

    def __init__(self):
        self.path = os.path.dirname(__file__)
        self.file_path = self.path + '/config/user_info.xlsx'
        self.file = xlrd.open_workbook(self.file_path)

    def change_float_string(self,val):      #处理excel文件的数据格式，默认都是浮点型，需要处理
        if isinstance(val,float):
            val = str(int(val))
        return val

    def get_sheet_info(self):
        user_list_key = ['account','password']
        user_list_data = []
        for row in range(1,self.sheet.nrows):   #excel的表头数据不用，从第二行开始，index就是从1开始
            info = [self.change_float_string(val) for val in self.sheet.row_values(row)]   #每一行的数据
            account_data = zip(user_list_key,info)   #解包组成字典
            user_list_data.append(dict(account_data))
        return user_list_data

    def get_sheetinfo_by_name(self,name):
        self.sheet = self.file.sheet_by_name(name)
        return self.get_sheet_info()

    def get_sheetinfo_by_index(self,index):
        self.sheet = self.file.sheet_by_index(index)
        return self.get_sheet_info()


if __name__ == '__main__':
    tt = Xlsx_Excel()
    info = tt.get_sheetinfo_by_index(0)
    print(info)
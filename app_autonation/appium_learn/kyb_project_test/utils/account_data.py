# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/4/22 3:58

import os
import xlrd

class Account_data(object):

    def __init__(self,data_file):
        self.path = os.path.dirname(os.path.dirname(__file__)) + '/data/'
        self.file_path = os.path.join(self.path,data_file)
        self.file = xlrd.open_workbook(self.file_path)

    def get_sheetinfo(self):
        #表头字段
        table_header = ['account','password']
        account_data = []
        for i in range(1,self.sheet.nrows):
            infos = [self.float_change_str(val) for val in self.sheet.row_values(i)]
            user_data = zip(table_header,infos)
            account_data.append(dict(user_data))
            # print(account_data)
        return account_data

    def get_sheetinfo_by_name(self,name):
        self.sheet = self.file.sheet_by_name(name)
        return self.get_sheetinfo()

    def get_sheetinfo_by_index(self,index):
        self.sheet = self.file.sheet_by_index(index)
        return self.get_sheetinfo()

    def float_change_str(self,val):
        """
        处理excel文件的数据格式，默认都是浮点型，需要处理
        :param val:
        :return:
        """
        if isinstance(val,float):
            val = str(int(val))
        return val

if __name__ == '__main__':
    dd = Account_data(data_file='account.xlsx')
    dd.get_sheetinfo_by_index(0)

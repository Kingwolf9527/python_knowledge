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
        #表头字段,一个列表
        table_header = self.sheet.row_values(0)
        account_data = []
        #不要表头字段，数据从第二行开始读取，index从1开始
        for i in range(1,self.sheet.nrows):
            #处理每一行的数据，把可能出现的浮点型数据转化为字符串
            infos_data = [self.float_change_str(val) for val in self.sheet.row_values(i)]
            if infos_data:
                #存储数据的字典
                user_data = {}
                for j in range(len(table_header)):   #表头有几列，字典有多少个键
                    user_data[table_header[j]] = infos_data[j]
            account_data.append(user_data)
            print(account_data)

            # #把info列表和表头字段组合，进行解包
            # user_data = zip(table_header,infos)
            # #把zip对象转为字典使用，最后把每一个元素追加到account_data里面，每个元素代表每一行数据
            # account_data.append(dict(user_data))
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

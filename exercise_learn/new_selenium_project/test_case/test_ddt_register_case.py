# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/12/2 23:12

import sys
sys.path.append(r'F:\Tortoise_python\exercise_learn\new_selenium_project')

import unittest
import ddt
from new_selenium_project.util.common_log import Common_Logs
from new_selenium_project.util.unittest_start_end import Unittest_start_end
from new_selenium_project.util.read_excel import Read_Excel


#实例化logger
log_name = Common_Logs(logger='register_test_case98235')
logger = log_name.get_logger()



#简单的ddt驱动数据
# ddt_data = [['111','test0047','test4007','djdj','user_email_error','请输入有效的电子邮件地址'],
#             ['@163.com','test0038','test008','djdj','user_email_error','请输入有效的电子邮件地址'],
#             ['1115411@163.com','tes3t009','test4009','djdj','user_email_error','请输入有效的电子邮件地址']]

#读取excel的数据
# ex = Read_Excel()
# ddt_data = ex.processing_data()

# @ddt.ddt
# class Ddt_register(Unittest_start_end):
#
#     @ddt.data(*ddt_data)
#
#     @ddt.unpack
#     def test_Register_case(self,*ddt_data):
#
#         # 利用list属性赋值
#         email, name, password, text_captcha, assertcode, asserttext = ddt_data
#         result_error = self._register_.register_fun(email, name, password, text_captcha, assertcode, asserttext)
#
#         self.assertIs(result_error, True, '测试失败！')




class Ddt_Register(Unittest_start_end):

    # 读取excel的数据
    ex = Read_Excel()

    def test_Register_case(self):

        #获取所有数据的行数
        rows = self.ex.get_nrows()
        if rows:
            for i in range(rows):
                #输入的信息
                email = self.ex.get_cell_value(i,self.ex.get_email_col())
                name = self.ex.get_cell_value(i,self.ex.get_username_col())
                password = self.ex.get_cell_value(i,self.ex.get_password_col())
                code = self.ex.get_cell_value(i,self.ex.get_code_col())
                error_type = self.ex.get_cell_value(i,self.ex.get_error_type_col())
                error_text = self.ex.get_cell_value(i,self.ex.get_error_text_col())

                #调用登录方法
                result_error = self.new_register_.register_fun(email,name,password,code,error_type,error_text)

                if result_error:
                    self.ex.write_value(i,6,'pass')
                else:
                    self.ex.write_value(i,6,'fail')







if __name__ == '__main__':
    unittest.main()
# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/6 3:53

from new_maizi_aututest.page_object.base_page import BasePage


# 登录页面
class Common_Login(BasePage):

    #账号，密码，按钮的元素
    account_loc = 'id=>id_account_l'
    password_loc = 'id=>id_password_l'
    button_loc = 'id=>login_btn'

    #输入账号
    def send_account(self,account):
        self.send_keys(self.account_loc,account)

    #输入密码
    def send_password(self,password):
        self.send_keys(self.password_loc,password)

    #点击按钮
    def click_button(self):
        self.click(self.button_loc)

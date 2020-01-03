# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/6 3:49

from new_maizi_aututest.page_object.base_page import BasePage


class Login_link_text(BasePage):

    btn_text = 'link_text=>登录'

    #点击登陆按钮，跳转登录页面
    def send_login_btn(self):
        self.click(self.btn_text)

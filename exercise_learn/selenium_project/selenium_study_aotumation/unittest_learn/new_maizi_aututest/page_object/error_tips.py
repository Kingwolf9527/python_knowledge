# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/7 4:11

from new_maizi_aututest.page_object.base_page import BasePage


class Error_tip(BasePage):

    error_tip_text = 'id=>login-form-tips'

    def error_text(self):
        self.screenshot_imgs()
        text = self.find_element(self.error_tip_text).text
        return text

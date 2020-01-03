# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/4/5 6:39

from appium_learn.page_object.base_view import Base
from appium_learn.utils.common_logs import Common_log
from appium_learn.utils.driver import Driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

logger = Common_log(logger='skip_btn').get_logger()

class Common_view(Base):

    skipbtn = (By.ID,'com.tal.kaoyan:id/tv_skip')

    #检测是否存在跳过按钮
    def check_skipbtn(self):
        logger.info('=================check skip_btn========================')
        try:
            # '跳过'按钮的定位
            skip_btn = self.driver.find_element(*self.skipbtn)
        except NoSuchElementException:
            logger.error('====================no shipbtn======================')
        else:
            skip_btn.click()
            logger.info('=====================pass the skip-page==================')


if __name__ == '__main__':
    driver = Driver().read_caps()
    com = Common_view(driver)
    com.check_skipbtn()
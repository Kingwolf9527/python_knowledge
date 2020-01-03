# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/4/16 4:50

from appium_learn.kyb_project_test.utils.driver import Driver
from appium_learn.kyb_project_test.utils.common_logs import Common_log
from appium_learn.kyb_project_test.page_object.baseView.common_view import Common_view
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import random

logger = Common_log(logger='regiser_action').get_logger()

class Register_View(Common_view):

    #注册按钮
    register_button = (By.ID,'com.tal.kaoyan:id/login_register_text')

    #注册页面-添加头像(这里需要判断权限问题)
    add_userheader = (By.ID,'com.tal.kaoyan:id/activity_register_userheader')

    #系统权限处理
    permission = (By.ID,'android:id/button1')
    uiautomator_loc1 = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("允许")')
    uiautomator_loc2 = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("确定")')
    uiautomator_loc3 = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("始终允许")')

    #添加图片
    header_images = (By.ID,'com.tal.kaoyan:id/iv_picture')
    # images = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tal.kaoyan:id/iv_picture")')
    finish_button = (By.ID,'com.tal.kaoyan:id/picture_tv_ok')
    # finish_button = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().textContains("完成")')
    varity_tailor = (By.ID,'com.tal.kaoyan:id/menu_crop')

    #账号，密码，邮箱
    username = (By.ID,'com.tal.kaoyan:id/activity_register_username_edittext')
    password = (By.ID,'com.tal.kaoyan:id/activity_register_password_edittext')
    email = (By.ID,'com.tal.kaoyan:id/activity_register_email_edittext')

    #立即注册按钮(这里需要做判断，可能会出现频繁注册被禁止)
    immediately_register_button = (By.ID,'com.tal.kaoyan:id/activity_register_register_btn')

    #判断是否出现频繁注册被限制的处理
    judge_ban_register = (By.ID,'com.tal.kaoyan:id/activity_perfectinfomation_major')

    #选择专业-具体专业-经济学(1)-统计管理学(2)-管理统计学(2)
    major = (By.ID,'com.tal.kaoyan:id/activity_perfectinfomation_major')
    subject_titles = (By.ID,'com.tal.kaoyan:id/major_subject_title')
    group_titles = (By.ID,'com.tal.kaoyan:id/major_group_title')
    search_item_names = (By.ID,'com.tal.kaoyan:id/major_search_item_name')

    #选择院校-添加院校按钮弹框处理(使用坐标法处理)-广东(需要上滑操作-13)-中山大学(0)
    perfectinfomation_school = (By.ID,'com.tal.kaoyan:id/activity_perfectinfomation_school')
    foum_titles = (By.ID,'com.tal.kaoyan:id/more_forum_title')
    university_names = (By.ID,'com.tal.kaoyan:id/university_search_item_name')
    # commit_select = (By.ID,'com.tal.kaoyan:id/activity_myinfo_addschool_commit')

    #进入考研帮按钮(需要判断是否注册成功(跟登录是否成功的校验一样))
    perfectinfomation_goBtn = (By.ID,'com.tal.kaoyan:id/activity_perfectinfomation_goBtn')

    #个人中心和昵称(校验注册是否成功)
    myself_button = (By.ID,'com.tal.kaoyan:id/mainactivity_button_mysefl')
    nickname = (By.ID,'com.tal.kaoyan:id/activity_usercenter_username')

    def register_action(self,username,password,email):
        #跳过引导页面
        self.check_skipbtn()

        logger.info('============================register action===========================')
        self.driver.find_element(*self.register_button).click()

        logger.info('===========================userheader setting=========================')
        #头像设置
        self.driver.find_element(*self.add_userheader).click()
        # 添加头像的权限判断(全部允许)
        try:
            eles = self.driver.find_elements(*self.permission)
            # 全部系统弹窗都点击允许
            for ele in eles:
                logger.info('===============permission setting==========================')
                if ele.text == u'允许':
                    self.driver.find_element(*self.uiautomator_loc1).click()
                elif ele.text == u'确定':
                    self.driver.find_element(*self.uiautomator_loc2).click()
                elif ele.text == u'始终允许':
                    self.driver.find_element(*self.uiautomator_loc3).click()
        except:
            logger.info('=======================No permission setting=============================')
            pass

        logger.info('==========================add images===================================')
        self.driver.implicitly_wait(5)
        #添加图片
        # WebDriverWait(self.driver,15,0.01).until(EC.presence_of_element_located(self.images))
        header_image = self.driver.find_elements(*self.header_images)
        header_image[2].click()
        # os.system('adb shell input tap 763 309')

        logger.info('==========================varity tailtor===============================')
        # WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.finish_button))
        time.sleep(2)
        #完成按钮和确定裁剪按钮
        self.driver.find_element(*self.finish_button).click()
        time.sleep(1)
        self.driver.find_element(*self.varity_tailor).click()

        #用户名，密码，邮箱
        self.driver.find_element(*self.username).send_keys(username)
        logger.info('register username is : %s' %username)
        time.sleep(1)

        self.driver.find_element(*self.password).send_keys(password)
        logger.info('register password is : %s' %password)
        time.sleep(1)

        self.driver.find_element(*self.email).send_keys(email)
        logger.info('register email is : %s' %email)

        logger.info('=====================click register button============================')
        self.driver.find_element(*self.immediately_register_button).click()
        #这里需要做判断，是否出现频繁注册被禁止的情况
        try:
            self.driver.find_element(*self.judge_ban_register)
        except NoSuchElementException:
            logger.error('===================register failed: regiser frequently================================')
            self.get_screenshot_image('register failed')
            return False
        else:
            #执行相应注册的操作
            self.add_register_info()
            #注册结果判断
            if self.register_status():
                return True
            else:
                return False

    def add_register_info(self):

        # 选择专业-具体专业-经济学(1)-统计管理学(2)-管理统计学(2)
        logger.info('====================select major============================')
        self.driver.find_element(*self.major).click()
        subject_title = self.driver.find_elements(*self.subject_titles)
        subject_title[1].click()

        group_title = self.driver.find_elements(*self.group_titles)
        group_title[2].click()

        item_name = self.driver.find_elements(*self.search_item_names)
        item_name[2].click()

        #选择院校
        logger.info('====================select school============================')
        self.driver.find_element(*self.perfectinfomation_school).click()

        #添加院校按钮-采用坐标法
        # os.system('adb shell input tap 190 1810')   #米8的定位坐标
        os.system('adb shell input tap 117 1083')    #模拟器的

        #选择省份-学校:广东(需要上滑操作 - 13) - 中山大学(0)
        foum_title = self.driver.find_elements(*self.foum_titles)
        time.sleep(2)
        # #上滑操作
        # self.swipe_up()
        foum_title[13].click()

        university_name = self.driver.find_elements(*self.university_names)
        university_name[0].click()

        time.sleep(2)
        # self.driver.find_element(*self.commit_select).click()
        os.system('adb shell input tap 666 959')    #选择院校后，点击确定按钮
        time.sleep(1)

        logger.info('============================click perfectinfomation_goBtn========================')
        #进入考研帮
        self.driver.find_element(*self.perfectinfomation_goBtn).click()


    def register_status(self):
        """
        判断注册是否成功，跟登录是否成功的校验一样
        :return:
        """
        logger.info('===========================register_status_check==============================')
        time.sleep(5)

        try:
            self.driver.find_element(*self.myself_button).click()
            # os.system('adb shell input tap 981 2082')   #米8的坐标定位
            time.sleep(3)
            self.driver.find_element(*self.nickname)
        except NoSuchElementException:
            logger.error('===========================register failed===============================')
            self.get_screenshot_image('Register Failed')
            return False
        else:
            logger.info('=============================register success=============================')
            self.get_screenshot_image('register success')
            return True


if __name__ == '__main__':
    driver = Driver().read_caps()
    register = Register_View(driver)
    #调试账号密码，邮箱
    username = 'king' + str(random.randint(10000,88888))
    password = 'king' + str(random.randint(1000,6666))
    email = 'wolf' + str(random.randint(100,777)) + '@163.com'
    register.register_action(username=username,password=password,email=email)








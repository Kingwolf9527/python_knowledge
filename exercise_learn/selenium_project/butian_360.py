# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/2 0:46

import os
import time
from selenium import webdriver
from PIL import Image
from baidu_ai.baidu_ai_api_test import BaiduOCR
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class Butian_proceing(object):

    def __init__(self):

        # 设置user-data-dir路径
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument('user-data-dir=F:\data_profile')
        driver_path = os.path.join((os.path.dirname(__file__)), 'selenium_study_aotumation', 'chromedriver.exe')
        self.driver = webdriver.Chrome(options=chrome_option, executable_path=driver_path)

        self.driver.get('https://www.butian.net/')

        # 让浏览器的窗口最大化
        self.driver.maximize_window()
        time.sleep(5)


    def get_captcha_img(self,full_captcha,small_captcha):

        #进入登录界面，先截完整图片
        self.driver.get_screenshot_as_file(full_captcha)
        time.sleep(1.5)

        #定位验证码图片
        captcha_img = self.driver.find_element_by_id('captchaImage')
        #获取验证码的四个坐标
        left = captcha_img.location['x']
        upper = captcha_img.location['y']
        right = captcha_img.size['width'] + left
        buttom = captcha_img.size['height'] + upper
        captcha_Coords = (left,upper,right,buttom)

        #打开完整截图
        img = Image.open(full_captcha)

        #先做灰度处理，再裁切
        pic = img.convert('L')
        new_img = pic.crop(captcha_Coords)
        new_img.save(small_captcha)


    def baidu_ocr(self,full_captcha,small_captcha):

        #先调用截图处理方法
        self.get_captcha_img(full_captcha,small_captcha)
        time.sleep(2)

        code = BaiduOCR().basic_Accurate_options(filepath=small_captcha)

        return code



    def butian(self,full_captcha,small_captcha):

        try:
            #定位到白帽登陆的界面
            self.driver.find_element_by_link_text(u'白帽登录').click()
            time.sleep(3)

            #关闭"重要提示"的alert弹窗(不能用传统的alert弹窗处理，还是用元素定位)
            # alert_window = driver.driver.switch_to.alert
            # alert_window.accept()
            #点击弹窗的"关闭按钮"
            alert_window = self.driver.find_element_by_xpath('//div[@id="mPrompt1"]//button[@class="btn-white"]').click()
            time.sleep(2)

            #跳转到360账号登录
            self.driver.find_element_by_link_text(u'使用360账号登录').click()
            time.sleep(2)

            #直接调用百度识别方法，获取验证码
            captcha_code = self.baidu_ocr(full_captcha,small_captcha)
            time.sleep(3)

            #使用360账号登录,输入账号密码
            self.driver.find_element_by_id('username').clear()
            self.driver.find_element_by_id('username').send_keys('lccr777@163.com')
            time.sleep(0.5)

            self.driver.find_element_by_id('password').clear()
            self.driver.find_element_by_id('password').send_keys('922521dfxs5619')
            time.sleep(2)

            #手动输入验证码(后续再接入百度识图的ai自动识别验证码)
            self.driver.find_element_by_id('captcha').clear()
            self.driver.find_element_by_id('captcha').send_keys(captcha_code)

            #点击登录按钮
            self.driver.find_element_by_id('button').click()
            time.sleep(3)

            #通过打印登录成功，跳转的页面右上角会显示用户昵称，判断该昵称是否一致来断定是否登录成功
            nickname = self.driver.find_element_by_xpath('//div[@class="whitehatName"]').text
            print(nickname)
            #右上角的账号
            username = self.driver.find_element_by_xpath('//a[@class="navtoolsName"]')
            if nickname == "狼胸_book14":
                print('登录成功')
                # #这里做一个退出登录的操作，涉及到鼠标悬停，目标是登录成功后的右上角昵称，鼠标悬停在这里，然后选择退出系统，点击结束
                # ActionChains(self.driver).move_to_element(username).perform()
                #
                # #定位到退出系统
                # logut = self.driver.find_element_by_link_text(u'退出系统')
                # logut.click()
                # time.sleep(3)
                # self.driver.quit()

                #如果登录成功，就尝试提交漏洞
                self.submit_vulnerability()
            else:
                print('登录失败')

        except Exception as e:
            print("错误的代码：",e)

    def submit_vulnerability(self):
        #点击"提交漏洞"
        self.driver.find_element_by_id('btnSub').click()
        time.sleep(2)

        #厂商名称
        self.driver.find_element_by_id('inputCompy').clear()
        self.driver.find_element_by_id('inputCompy').send_keys('test')

        #域名或者ip
        self.driver.find_element_by_name('host').clear()
        self.driver.find_element_by_name('host').send_keys('11111')

        #漏洞类型(下拉框属于select方法)---选择"web漏洞",index=1，value=1
        selection = Select(self.driver.find_element_by_id('selCate'))
        selection.select_by_visible_text('Web漏洞')

        #漏洞标题
        self.driver.find_element_by_xpath('//input[@id="title"]').clear()
        self.driver.find_element_by_xpath('//input[@id="title"]').send_keys('222有SQL注入')

        #漏洞url
        self.driver.find_element_by_name('url[]').clear()
        self.driver.find_element_by_name('url[]').send_keys('http://12356.com')

        #漏洞类型(一般都是事件型)--一般批量都是SQL注入，中危
        vulner_type = Select(self.driver.find_element_by_id('lootypesel2'))
        vulner_type.select_by_visible_text('SQL注入')

        #漏洞等级
        vulner_level = Select(self.driver.find_element_by_name('level'))
        vulner_level.select_by_visible_text('中危')

        #简要描述
        self.driver.find_element_by_id('description').clear()
        self.driver.find_element_by_id('description').send_keys('777777777777777777777')

        #详细细节(暂时还是手动处理比较好),这里的编辑器嵌套了iframe表单，需要先处理
        self.driver.switch_to.frame('ueditor_0')
        self.driver.find_element_by_xpath('//body[@class="view"]').clear()
        self.driver.find_element_by_xpath('//body[@class="view"]').send_keys('第一次测试调试！')


        # time.sleep(120)

        #修复方案
        self.driver.find_element_by_id('repair_suggest').clear()
        self.driver.find_element_by_id('repair_suggest').send_keys('过滤相关关键字')

        #所属行业(一般选择"IT/计算机/互联网/通信")
        industry = Select(self.driver.find_element_by_id('industry1'))
        industry.select_by_visible_text('IT/计算机/互联网/通信')

        #行业分类(默认选择第一个选项)
        self.driver.find_element_by_xpath('//p[@id="industry2"]//input[@id="19"]').click()

        #所属地区，分省市县三个下拉框
        province_selection = Select(self.driver.find_element_by_id('selec1'))
        province_selection.select_by_visible_text('广东省')

        city_selection = Select(self.driver.find_element_by_id('selec2'))
        city_selection.select_by_visible_text('珠海市')

        country_selection = Select(self.driver.find_element_by_id('selec3'))
        country_selection.select_by_visible_text('市辖区')

        #厂商联系方式
        self.driver.find_element_by_name('company_contact').clear()
        self.driver.find_element_by_name('company_contact').send_keys('Tel：0759-2222222')

        #匿名提交
        self.driver.find_element_by_name('anonymous').click()

        #点击提交按钮
        self.driver.find_element_by_id('tijiao').click()

        #这里的滑块拖动或者点击文字，还是要手动
        time.sleep(15)



if __name__ == "__main__":
    butian_ = Butian_proceing()
    butian_.butian(full_captcha=r"E:\selenium_pic\full_captcha.png",small_captcha=r"E:\selenium_pic\small_captcha.png")



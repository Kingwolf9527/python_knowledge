# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/12 15:35

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

def PMS():

    driver = webdriver.Chrome()
    driver.get('https://fangqian.st.anhouse.com.cn/login.html')
    time.sleep(2)
    #窗口最大化
    driver.maximize_window()

    try:

        '''
            登陆:包括安全码，账号，密码
            
        '''
        #安全码
        driver.find_element_by_id('anQuanMa').clear()
        driver.find_element_by_id('anQuanMa').send_keys('010110304')
        time.sleep(1)

        #账号
        driver.find_element_by_id('userName').clear()
        driver.find_element_by_id('userName').send_keys('admin')
        time.sleep(1)

        #密码
        driver.find_element_by_id('passWord').clear()
        driver.find_element_by_id('passWord').send_keys('123456')
        time.sleep(1)

        #登陆按钮
        driver.find_element_by_xpath('//button[@onclick="login()"]').click()
        time.sleep(5)

        #先定位到设置，再对子菜单选择,需要鼠标悬停
        setting = driver.find_element_by_link_text(u'设置')
        ActionChains(driver).move_to_element(setting).perform()
        #定位到角色管理
        role_manage = driver.find_element_by_xpath('//li[@roleaccess="fq_pz_jsgl"]')
        role_manage.click()
        time.sleep(3)

        #添加角色
        driver.find_element_by_id('addJueSe').click()
        time.sleep(1)

        #切换到iframe
        driver.switch_to_default_content()   #切换到top层
        driver.switch_to_frame("main-content")
        # 弹出框的iframe在第二层，需要再切进去一层
        driver.switch_to_frame("layui-layer-iframe2")
        time.sleep(2)

        #弹出框的角色名称和描述
        driver.find_element_by_xpath('//input[@id="name"]').send_keys('工程师777777')
        driver.find_element_by_xpath('//input[@id="desc"]').send_keys('代码仔，最劲！！！')
        time.sleep(2)
        #保存按钮
        driver.find_element_by_xpath('//button[@onclick="saveJueSe()"]').click()
        time.sleep(2)

        #需要重新退出上面iframe，重新进入相关页面
        driver.switch_to_default_content()   #切换到top层
        driver.switch_to_frame("main-content")

        #修改权限
        driver.find_element_by_xpath('//span[@roleaccess="fq_pz_jsgl_xgqx"]').click()
        time.sleep(4)

        #再退出iframe框架到top层，再切换到新的不同窗口的iframe层级去
        driver.switch_to_default_content()
        xpath = driver.find_element_by_xpath('//div[@class="layui-layer-content"]/iframe')
        driver.switch_to_frame(xpath)

        #切换不同权限的窗口
        driver.find_element_by_link_text(u'合同').click()
        time.sleep(5)
        driver.find_element_by_link_text(u'工作台').click()
        time.sleep(5)

        #切换到top层,因为弹窗右上角的关闭按钮是在top层
        driver.switch_to_default_content()

        # 关闭修改权限的窗口，两种方式定位，xpath和CSS的
        driver.find_element_by_xpath(
            '//span[@class="layui-layer-setwin"]/a[@class="layui-layer-ico layui-layer-close layui-layer-close1"]').click()
        # driver.find_element_by_css_selector('[class="layui-layer-setwin"]').click()
        driver.quit()

    except Exception as e:
        print("错误的代码：",e)
        time.sleep(3)
        driver.quit()

if __name__ == '__main__':
    PMS()


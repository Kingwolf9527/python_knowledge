# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/1/22 20:49

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def baidu_serach():

    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir=F:\profile')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://www.baidu.com')

    driver.find_element_by_id('kw').send_keys('热血江湖')
    driver.find_element_by_id('su').click()

    WebDriverWait(driver,15).until(EC.title_contains('热血江湖'))

    current_handle = driver.current_window_handle
    print(current_handle)

    driver.find_element_by_xpath('//div[@id="content_left"]/div[@id="1"]/h3[@class="t"]/a[contains(text(),"官方网站")]').click()

    handles = driver.window_handles
    print(handles)
    for handle in handles:
        if handle != current_handle:
            driver.switch_to.window(handle)
            # driver.switch_to_window(handle)   #这个不建议使用了，采用新的方法

            WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//div[@class="drop_down"]/a/h2[contains(@class,"top_nav_game")]')))

            url = driver.current_url
            if url == 'http://rxjh.cdcgames.net/':
                print('欢迎进入热血江湖官方网站！')
    driver.quit()

if __name__ == '__main__':
    baidu_serach()
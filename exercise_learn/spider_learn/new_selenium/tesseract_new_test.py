# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/12/12 3:37

import pytesseract
from PIL import Image
import time
from urllib import request

def main():

    pytesseract.pytesseract.tesseract_cmd = r'F:\tesseract-ocr\tesseract.exe'
    #获取验证码的请求url
    url = 'https://passport.360.cn/captcha.php?m=create&app=i360&scene=login&userip=&level=default&sign=8820a4&r=1544557887&_=1544557885428'

    while True:
        request.urlretrieve(url,'F:\capt.jpg')
        image = Image.open('F:\capt.jpg')
        text = pytesseract.image_to_string(image)
        print(text)
        time.sleep(2)


if __name__ == '__main__':
    main()







    # #判断是否存在验证码
    # captcha = driver.find_element_by_xpath('//img[@class="quc-captcha-img quc-captcha-change"]').get_attribute('src')
    # print(captcha)
    #
    # #浏览器页面截图
    # driver.get_screenshot_as_file(screen_img)
    #
    # #定位验证码的位置和大小
    # location = driver.find_element_by_xpath('//img[@class="quc-captcha-img quc-captcha-change"]').location
    # size = driver.find_element_by_xpath('//img[@class="quc-captcha-img quc-captcha-change"]').size
    # left = location['x']
    # top = location['y']
    # right = location['x'] + size['width']
    # buttom = location['y'] + size['height']
    #
    # # 从文件读取截图，截取验证码位置再次保存
    # # left, top, right, bottom = int(left), int(top), int(right), int(buttom)
    # img = Image.open(screen_img)
    # img.crop((left,top,right,buttom))
    # img = img.convert('L')     #转换模式：L | RGB
    # img = ImageEnhance.Contrast(img)      #增强对比度
    # img = img.enhance(2.0)       #增加饱和度
    # # img.load()    # 对比度增强
    # img.save(screen_img)
    # time.sleep(3)
    # print(img)
    #
    # # 再次读取识别验证码
    # img = Image.open(screen_img)
    # time.sleep(3)
    # code = pytesseract.image_to_string(img).strip()
    # # 5、收到验证码，进行输入验证
    # print(code)
    # driver.find_element_by_xpath('//input[@class="quc-input quc-input-captcha"]').send_keys(code)

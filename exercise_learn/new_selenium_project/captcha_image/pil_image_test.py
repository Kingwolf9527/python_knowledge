# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/11/14 16:12

from PIL import Image


im = Image.open(r"E:\selenium_pic\register_captcha.png")
pic = im.crop((714, 523, 843, 563))
pic.save(r'E:\selenium_pic\register_captcha_small.png')
pic.show()

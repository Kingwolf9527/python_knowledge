# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/11/13 1:11


import pytesseract
from PIL import Image


image = Image.open("captcha_1.png")

#这个方法主要用在规则文字，数字，字符串等等，如果扭曲很大，变形严重，识别成功率低
text = pytesseract.image_to_string(image)
print(text)
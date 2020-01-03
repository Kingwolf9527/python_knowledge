# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/13 15:30

import pytesseract
from PIL import Image

img = Image.open(r'F:\tesseract-ocr\tessdata\5.png')

code_ = pytesseract.image_to_string(img,lang='chi_sim')

print(code_)
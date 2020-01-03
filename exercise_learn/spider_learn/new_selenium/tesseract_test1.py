# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/12/12 3:21

import pytesseract
from PIL import Image


#指定tesseract执行文件的具体路径
pytesseract.pytesseract.tesseract_cmd = r'F:\tesseract-ocr\tesseract.exe'

#打开图片文件
image = Image.open(r'F:\2.png')

#把图片转为字符串
text = pytesseract.image_to_string(image,lang='chi_sim')

print(text)
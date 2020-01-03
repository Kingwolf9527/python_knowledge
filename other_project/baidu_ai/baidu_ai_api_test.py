# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/12/22 2:59



"""

    详情API查看地址：https://ai.baidu.com/docs#/OCR-Python-SDK/top


"""

from aip import AipOcr

class BaiduOCR(object):

    def __init__(self,APP_ID='11223350',API_Key='K0QoGISeULWbNNr3sYYNDchA',Secret_Key='5kLp3QYL8rMEUh6ooiLGjXhrXW1ZxUF2'):
        """

        :param APP_ID: 你的 App ID
        :param API_Key: 你的 Api Key
        :param Secret_Key: 你的 Secret Key
        :param 这些参数设置可以在：百度云控制台/AI服务控制台中的应用列表  查看
        """

        #配置AipOcr
        self.APP_ID = APP_ID
        self.API_Key = API_Key
        self.Secret_Key = Secret_Key

        #调用OCR服务
        self.client = AipOcr(self.APP_ID,self.API_Key,self.Secret_Key)

    def get_file_content(self,filepath):
        """
        读取图片
        :param filepath:
        :return:
        """
        with open(filepath,'rb') as fp:
            return fp.read()


    def base_general(self,filepath):
        """
        调用通用文字识别, 图片参数为本地图片(不带可选参数)
        :return:
        """
        image = self.get_file_content(filepath)
        img =  self.client.basicGeneral(image)
        #打印识别结果
        code = img['words_result'][0]['words']
        return code

    def base_general_options(self,filepath):
        """
        带参数调用通用文字识别, 图片参数为本地图片
        :return:
        """
        #有可选参数
        options = {}
        options['detect_direction'] ='true'
        options['probability'] = 'true'

        image = self.get_file_content(filepath)
        img =  self.client.basicGeneral(image,options)
        #打印识别结果
        code = img['words_result'][0]['words']
        return code


    def basic_Accurate_options(self,filepath):
        """
        有可选参数,通用文字识别（高精度版）
        :return:
        """
        # 有可选参数
        options = {}
        options['detect_direction'] = 'true'
        options['probability'] = 'true'


        #采用高精度的
        image = self.get_file_content(filepath)
        img = self.client.basicAccurate(image,options)
        #打印识别结果
        code = img['words_result'][0]['words']
        print("验证码结果是：%s" %code)
        return code



if __name__ == '__main__':

    #识别的图片路径
    pic_path = r'E:\selenium_pic\register_captcha_small.png'
    basic = BaiduOCR()
    basic.basic_Accurate_options(filepath=pic_path)
    # basic.base_general_options(filepath=pic_path)
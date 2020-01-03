# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/12/22 2:44
import requests

headers = {

    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Content-Type' : 'application/json; charset=UTF-8'
}

url = 'https://aip.baidubce.com/oauth/2.0/token'

data = {

    'grant_type' : 'client_credentials',
    'client_id' : 'K0QoGISeULWbNNr3sYYNDchA',                  #应用的API Key
    'client_secret' : '5kLp3QYL8rMEUh6ooiLGjXhrXW1ZxUF2'      #应用的Secret Key
}

response = requests.post(url,data=data,headers=headers)
access_token_content = response.text
print(access_token_content)

"""
    API服务器返回的信息：
    {
        "refresh_token":"25.cf8051fc8c084973f447d126d384836d.315360000.1860778404.282335-11223350",
        "expires_in":2592000,
        "session_key":"9mzdCKZ3hXy1rry7065FUmqjlh0dGWBWE2zuQwHNGeV+HN+jd+UMrCqUuogu2cL1zcBdEphmS1wrNzw95HVtG3H+4Lj5EQ==",
        "access_token":"24.3bf14b36937b6fbae68e2aa3a14a32f9.2592000.1548010404.282335-11223350",
        "scope":"brain_ocr_train_ticket brain_ocr_taxi_receipt brain_numbers brain_ocr_vat_invoice brain_ocr_handwriting public vis-ocr_ocr brain_ocr_scope brain_ocr_general brain_ocr_general_basic brain_ocr_general_enhanced vis-ocr_business_license brain_ocr_webimage brain_all_scope brain_ocr_idcard brain_ocr_driving_license brain_ocr_vehicle_license vis-ocr_plate_number brain_solution brain_ocr_plate_number brain_ocr_accurate brain_ocr_accurate_basic brain_ocr_receipt brain_ocr_business_license brain_solution_iocr wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test权限 vis-classify_flower lpq_开放 cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify",
        "session_secret":"d7992c1efe899ff09d59fa011d8c555b"
    }
    
    ：：access_token： 要获取的Access Token；
    ：：expires_in： Access Token的有效期(秒为单位，一般为1个月)；    主要用这两个参数

    百度API的详细文档，参考这个：http://ai.baidu.com/docs#/Auth/top

"""
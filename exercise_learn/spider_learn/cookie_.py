# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/18 23:57

'''
    因为http协议是无状态的，cookie的出现就是为了解决这个问题的，而且cookie存储的数据量有限，一般不超过4KB
    cookie的格式解释：
    Set-Cookie:name=value；expires/max-age=date;path=path;domain=damain_name;secury
    name:cookie的名字
    value:cookie的值
    expires/max-age:cookie的过期时间
    path:cookie作用的路径，默认是根目录，例如：path=/
    domain:cookie作用的域名，默认是主域名，例如：Domain=www.xxx.com,如果像所有子域名都作用到，可以这样设置：Domain=.xxx.com
    secury:是否只在https协议下起作用

'''

#163邮箱的收件箱url：http://mail.163.com/js6/main.jsp?sid=wAYrvEUAfCCmJIHwvpAAVKJQjsFxPABJ&df=163navi#module=mbox.ListModule%7C%7B%22fid%22%3A1%2C%22order%22%3A%22date%22%2C%22desc%22%3Atrue%7D
#163邮箱的登录url：https://mail.163.com/

from urllib import request

#不使用cookie去请求收件箱
mail_url = 'http://mail.163.com/js6/main.jsp?sid=wAYrvEUAfCCmJIHwvpAAVKJQjsFxPABJ&df=163navi#module=mbox.ListModule%7C%7B%22fid%22%3A1%2C%22order%22%3A%22date%22%2C%22desc%22%3Atrue%7D'

# headers = {
#
#     'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
#
# }

#使用cookie的情况下，cookie是存储在浏览器本地，也放在request的请求头中，注意cookie的名字是区分大小写的
headers = {

    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Cookie' : '_ntes_nnid=f31a53d859fd0f1dfa610fc1d644d3d6,1527695179544; _ntes_nuid=f31a53d859fd0f1dfa610fc1d644d3d6; vjuids=-3dec0cf97.163ef261936.0.7db7721a4d5c7; __gads=ID=40398bc3766e425d:T=1528725641:S=ALNI_MaBWDDaApPYsdmFROTTS_F2FNau_A; locale=; mail_psc_fingerprint=a4d7ae66012543e1a7ea9acde07566c8; usertrack=O2+gylsegLsLrkMPAw8EAg==; __yadk_uid=69d8vTjd6eeeO8v8Hg8igkKJPHc4s0wC; UM_distinctid=163f35b079d378-0648e27f05ce1b-5f4f2c16-100200-163f35b07a02b4; NTES_CMT_USER_INFO=72051747%7Clccr777%7C%7Cfalse%7CbGNjcjc3N0AxNjMuY29t; _ga=GA1.2.1198215468.1531065704; nts_mail_user=lccr777@163.com:-1:1; vjlast=1528725642.1538077382.12; vinfo_n_f_l_n3=f50e2a4fe58969e0.1.7.1528796220735.1537264660351.1538077382654; __f_=1540978033339; hb_MA-BFF5-63705950A31C_source=mooc.study.163.com; Province=020; City=0756; NNSSPID=c8fab84a09584fcfb0499d0387c33d36; NTES_hp_textlink1=old; n_ht_s=1; ntes_misc=0||10#0|0|011020|0|163||0d8f2957b8d860a721e0f7edbc1379d4; cm_newmsg=user%3Dlccr777%40163.com%26new%3D39%26total%3D289; mail_upx_nf=; mail_idc=; Coremail=0667f0ceb4bcc%wAYrvEUAfCCmJIHwvpAAVKJQjsFxPABJ%g5a45.mail.163.com; MAIL_MISC=lccr777; cm_last_info=dT1sY2NyNzc3JTQwMTYzLmNvbSZkPWh0dHAlM0ElMkYlMkZtYWlsLjE2My5jb20lMkZqczYlMkZtYWluLmpzcCUzRnNpZCUzRHdBWXJ2RVVBZkNDbUpJSHd2cEFBVktKUWpzRnhQQUJKJnM9d0FZcnZFVUFmQ0NtSklId3ZwQUFWS0pRanNGeFBBQkomaD1odHRwJTNBJTJGJTJGbWFpbC4xNjMuY29tJTJGanM2JTJGbWFpbi5qc3AlM0ZzaWQlM0R3QVlydkVVQWZDQ21KSUh3dnBBQVZLSlFqc0Z4UEFCSiZ3PW1haWwuMTYzLmNvbSZsPS0xJnQ9LTE=; secu_info=1; Coremail.sid=wAYrvEUAfCCmJIHwvpAAVKJQjsFxPABJ; mail_style=js6; mail_uid=lccr777@163.com; mail_host=mail.163.com; starttime=; mail_login_way=normal; NTES_SESS=yQcZ1Z3sDzq21DQtyyl.61RZXQU0jgxayfRS9A0ufGMD490e4zw3CZ7ZfG7r7Q1lJz48iIdDIiZpLXG_3HwWhFn4rxOTkwdMiOrhhyuu97eGBuW2xYYI6ehdTPNTFT6Mss8gkmoOwzYfEIxkvhfjxjN6mjh3MKHtcZD9_YaP4v60cxya8lFhYp4m4WPEkTsMG; S_INFO=1542559284|0|3&100##|lccr777; P_INFO=lccr777@163.com|1542559284|0|163|00&99|gud&1542557997&163#gud&440400#10#0#0|&0|163&blog|lccr777@163.com; mail_upx=t1gd.mail.163.com|t2gd.mail.163.com|t3gd.mail.163.com|t4gd.mail.163.com|t1bj.mail.163.com|t2bj.mail.163.com|t3bj.mail.163.com|t4bj.mail.163.com; MAIL_SESS=yQcZ1Z3sDzq21DQtyyl.61RZXQU0jgxayfRS9A0ufGMD490e4zw3CZ7ZfG7r7Q1lJz48iIdDIiZpLXG_3HwWhFn4rxOTkwdMiOrhhyuu97eGBuW2xYYI6ehdTPNTFT6Mss8gkmoOwzYfEIxkvhfjxjN6mjh3MKHtcZD9_YaP4v60cxya8lFhYp4m4WPEkTsMG; MAIL_SINFO=1542559284|0|3&100##|lccr777; MAIL_PINFO=lccr777@163.com|1542559284|0|163|00&99|gud&1542557997&163#gud&440400#10#0#0|&0|163&blog|lccr777@163.com; mail_entry_sess=6caf4ae13b939f7a8af47cb93a214b2aebb1a2cb5c9de21cf68f3d21bb70f3624045271aa838b313e5721d055c991b3a6fc78106fae3efb1c6fde7bccce591537dd1f386fe52bcbe311e24fd87b2de2c15c2b727f53975e29810cfb03d6271f25dd778d4f10a7f49f6937f0893f757de93f020dc875532b11ae8f0e573d461df41611ec7e030e418240a16a1cf9b83cf3377235abf56486e267cda1dd45774487a2fde0240eed65e6dac612ae6e6ec64f71e5803f4e59b83d60659f59496e611; JSESSIONID=B8CEBC0826565656AB04795BC7216414'
}

res = request.Request(mail_url,headers=headers)
resp = request.urlopen(res)
# print(resp.read().decode('utf-8'))
#返回的是登录的页面，无法直接访问到个人中心的收件箱

#把返回的数据写到本地，以HTML形式保存
with open('mail2.html','w',encoding='utf-8') as f:
    '''
        ::write函数必须写入一个str的数据类型
        ::resp.read()读出来的是一个bytes数据类型
        ::bytes -> decode -> str   涉及到Unicode的转换
        ::str   -> encode -> bytes
    
    '''
    f.write(resp.read().decode('utf-8'))
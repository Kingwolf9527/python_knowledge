#- * - coding:utf-8
#__author__ : kingwolf
#createtime : 2020/1/18 2:10

import time
import threading
import requests


def douyuUserInfo():

    headers = {
       'accept' : 'application/json, text/plain, */*',
       'accept-language' : 'zh-CN,zh;q=0.9',
       'content-type' : 'application/x-www-form-urlencoded',
       'origin' : 'https://www.douyu.com',
       'referer' : 'https://www.douyu.com/99999',
       'sec-fetch-mode' : 'cors',
       'sec-fetch-site' : 'same-origin',
       'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
       'x-requested-with' : 'XMLHttpRequest',
       'cookie' : 'smidV2=2018062619203798039b57ecac2247fce2cdb3c96985b60010b8103f954af70; dy_did=f91d42f28252e4d62504aa4f27061501; _ga=GA1.2.44940914.1540536798; acf_devid=8462ea135ef15a219373680d4a310d88; acf_did=f91d42f28252e4d62504aa4f27061501; acf_auth=85289RoDU5GRfw29Og42Yx5qLDOxK3MJrkgp1FszEqi3xArZl5Ci8Y%2BwOPXk5pTuLfPFlf1BxoN7ROp8zzjZv%2FM0crGyRMaIvCl1hsi7O2egD2FGgZmnFBmv; dy_auth=aa625COJ3MLwUi9o1BUb9iQEmO7Ea1y6nvR94EbXhFMuac3YIeYW58UwlAYxQfn1qWDuRQMiD8eUfclWjQ%2BYFPgPQXppuRbMY%2BIlRn35WAMU2abthxg%2Bsud4; wan_auth37wan=8714144a6f83qCt0TgDbXPP2Uwp9JT%2B6oAu9Q1XVto1CApoyx5JF8rhULH1R1zZUZfnvS%2BFz7vYGSEVjXTLMMIOywgTl0h2qwylwIMtYUbcEHjZl5w; acf_uid=24773511; acf_username=qq_nzGIlCMR; acf_nickname=%E7%8B%BC%E4%BA%BA%E6%9C%AC%E8%89%B2; acf_own_room=0; acf_groupid=1; acf_phonestatus=1; acf_ct=0; acf_ltkid=89090884; acf_biz=1; acf_stk=d1bbee2f0e879dd0; acf_avatar=//apic.douyucdn.cn/upload/avatar/024/77/35/11_avatar_; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1578900748,1578989940,1579098237,1579251679; PHPSESSID=fli362r56gdgt0hbohsrvua324; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1579283573'

    }

    data = {

        'propId' : 5,
        'propCount' : 1,
        'roomId' : 99999,
        'bizExt' : {"yzxq": {}}
    }

    url = 'https://www.douyu.com/japi/prop/donate/mainsite/v1'

    userDaa = requests.post(url=url,headers=headers,data=data).text
    print(userDaa)


def donateGiftThreading():

    for i in range(5):
        try:

            threading.Thread(target=douyuUserInfo).start()
        except Exception as e:
            print(e)



donateGiftThreading()
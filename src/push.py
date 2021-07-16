import requests
import re
import os

SKEY = ""  # Qmsg酱
urlSKEY = ""
boturl = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=56902235-478e-4fe4-8cab-a64e5776b81f"
if "urlSKEY" in os.environ and os.environ["urlSKEY"]:
    urlSKEY = os.environ["urlSKEY"]
    print("可以选择企业bot推送")

if "SKEY" in os.environ and os.environ["SKEY"]:
    SKEY = os.environ["SKEY"]
    print("可以选择Qmsg酱推送")

if "boturl" in os.environ and os.environ["boturl"]:
    boturl = os.environ["boturl"]
    print("可以选择群消息推送")

# 利用Qmsg酱推送到QQ上


def push(notion):
    if SKEY:
        url = "https://qmsg.zendee.cn/send/"+SKEY
        data = {
            "msg": notion
        }
        response = requests.post(url=url, data=data)
        if(response.status_code == 200):
            print("Qmsg酱送成功")
    if urlSKEY:
        data = {
            "msg": notion
        }
        response = requests.get(urlSKEY, params=data)
        if(response.status_code == 200):
            print("企业机器人推送成功")


def botpush(data):
    if boturl:
        response = requests.post(boturl,data=data)
    if (response.status_code == 200):
        print("群组消息推送成功")

    return response.status_code

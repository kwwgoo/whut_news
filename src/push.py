import requests
import re
import os

SKEY = ""  # Qmsg酱
urlSKEY = ""
boturl = ""
if "urlSKEY" in os.environ and os.environ["urlSKEY"]:
    urlSKEY = os.environ["urlSKEY"]
    print("选择企业bot推送")

if "SKEY" in os.environ and os.environ["SKEY"]:
    SKEY = os.environ["SKEY"]
    print("选择Qmsg酱推送")
if "boturl" in os.environ and os.environ["boturl"]:
    boturl = os.environ["boturl"]
    print("群消息推送")

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


def boturl(headers, data):
    if boturl:
        response = requests.post(boturl, headers=headers, data=data)
    if (response.status_code == 200):
        print("群组消息推送成功")

    return response.status_code

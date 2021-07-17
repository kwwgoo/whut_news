import requests
import re
import os
import json

id = "ww25c38dc950aba839"
secert = "IKnzzfncxbXSpmW25tvhMBhfgUvZ8j5F70LaxRiePtc"
agentId = "1000004"
SKEY = ""  # Qmsg酱
urlSKEY = ""
boturl = ""

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


def Qsmgpush(notion):
    if SKEY:
        url = "https://qmsg.zendee.cn/send/"+SKEY
        data = {
            "msg": notion
        }
        response = requests.post(url=url, data=data)
        if(response.status_code == 200):
            print("Qmsg酱送成功")




def weipush(data,id=id,secert=secert,agentID=agentId):
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=" + id + "&corpsecret=" + secert
    r = requests.get(url)
    tocken_json = json.loads(r.text)
    response = sendText(tocken=tocken_json['access_token'],agentId=agentId,data=data)
    if(response.status_code==200):
        print("企业应用机器人推送成功")
    return response

def botpush(data):
    if boturl:
        response = requests.post(boturl,data=data)
    if(response.status_code == 200):
        print("群组消息推送成功")
    return response

def sendText(tocken,agentId,data):
    data = json.loads(data)
    data['agentid'] = agentId
    data['touser'] = "@all"
    data = json.dumps(data)
    sendUrl = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + tocken
    response=requests.post(sendUrl,data)
    return response

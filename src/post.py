# 体温上报小程序
import requests
import json
from push import weipush
a = ""
url = "https://zhxg.whut.edu.cn/yqtjwx/monitorRegister"
headers = {"Connection": "keep-alive",
           "X-Tag": "flyio",
           "content-type": "application/json",
           "Cookie": "JSESSIONID=896e9434-18b0-422d-8eb9-97cffb20c363",
           "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.9(0x18000924) NetType/WIFI Language/zh_CN",
           "Referer": "https://servicewechat.com/wxa0738e54aae84423/11/page-frame.html",
           }
data = json.dumps({
    "diagnosisName": "", "relationWithOwn": "", "currentAddress": "湖北省武汉市洪山区岭南路", "remark": "", "healthInfo": "正常", "isDiagnosis": 0, "isFever": 0, "isInSchool": 0, "isLeaveChengdu": 0, "isSymptom": "0", "temperature": "36°C以下", "province": "湖北省", "city": "武汉市", "county": "洪山区",

})

response = requests.post(url, headers=headers, data=data)
print(response.json())
status = response.json()["status"]
if(status == "true"):
    a = "今天体温上报成功"
else:
    a="体温已经上报或者上报失败"

data = json.dumps({
    "safe": 0,
    "touser": "@all",
    "msgtype": "text",
    "text": {
        "content":a }
})
weipush(data)
import requests
import json

def getTocken(id,secert,agentId,data):
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=" + id + "&corpsecret=" + secert
    r = requests.get(url)
    tocken_json = json.loads(r.text)
    response=sendText(tocken=tocken_json['access_token'],agentId=agentId,data=data)
    return response.status_code

def sendText(tocken,agentId,data):
    sendUrl = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + tocken
    respoense=requests.post(sendUrl,data)
    return respoense

def getusersid(tocken):
    sendUrl = "https://qyapi.weixin.qq.com/cgi-bin/user/getuserid?access_token=" + tocken
    data = {"mobile": "16671048689"}
    requests.post(sendUrl, data=data)

def upload(tocken):  # 上传素材
    url = "https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token="+tocken
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    filename = '.\image\1.jpg'
    data = {
        "Content-Disposition": "form-data; name='fieldNameHere'; filename",
        "Content-Type": "image/jpg",
        "Content-Length": "220",
    }
    response = requests.post(url, headers=headers, data=data)
    print(response.text)


if __name__ == "__main__":
    getTocken(id, secert, agentId, data)

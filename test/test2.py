import requests
import json
from whether import get_time, get_content
id = "ww25c38dc950aba839"
secert = "IKnzzfncxbXSpmW25tvhMBhfgUvZ8j5F70LaxRiePtc"
agentId = "1000004"


def getTocken(id, secert, agentId):
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=" + \
        id + "&corpsecret=" + secert

    r = requests.get(url)
    tocken_json = json.loads(r.text)
    # sendText(tocken=tocken_json['access_token'],agentId=agentId,msg=msg)
    # article(tocken=tocken_json['access_token'],agentId=agentId)
    #textcard(tocken=tocken_json['access_token'], agentId=agentId)
    r=markdown(tocken=tocken_json['access_token'], agentId=agentId)
    # respense=getusersid(tocken=tocken_json['access_token'])



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


def textcard(tocken, agentId):
    sendUrl = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + tocken
    data = json.dumps({
        "touser": "@all",
        "msgtype": "textcard",
        "agentid": agentId,
        "textcard": {
            "title": "文本卡片测试通知",
            "description": "<div class=\"gray\">2021年7月16日</div> <div class=\"normal\">恭喜韩玺廷，于黎辉，邓永禧同学抽中iPhone 12一台，领奖码：ojbk</div><div class=\"highlight\">请于2222年02月22日后找汪凯伟同学领取</div>",
            "url": "https://staticedu-wps.cache.iciba.com/image/d54b825982313e31a34efe6d51f851bd.png",
            "btntxt": "测试文本卡片消息的"
        },
        "enable_id_trans": 0,
        "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800
    })
    requests.post(sendUrl, data)


def article(tocken, agentId):
    sendUrl = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + tocken
    # print(sendUrl)
    data = json.dumps({
        "touser": "@all",
        "msgtype": "news",
        "agentid": agentId,
        "news": {
            "articles": [
                {
                    "title": "测试图文消息",
                    "description": "今天是个好日子",
                    "url": "URL",
                    "picurl": "https://staticedu-wps.cache.iciba.com/image/d54b825982313e31a34efe6d51f851bd.png"
                }
            ]
        },
        "enable_id_trans": 0,
        "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800
    })
    requests.post(sendUrl, data)


def markdown(tocken, agentId):
    sendUrl = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + tocken
    # print(sendUrl)
    time, count_down = get_time()
    jitang, translation, image_url = get_content()
    content = jitang, translation
    data = json.dumps({
        "touser": "@all",
        "msgtype": "markdown",
        "agentid": 1,
        "markdown": {
            "content": 
            '''
            考研倒计时
            > **事项详情 **
            >离考研还有：<< font color=\"info\"> count_down天 < /font >
            >参与者：@ 韩玺廷、@ 邓永禧、@ 汪凯伟
            >日　期：< font color=\"warning\"> time < /font >
            >时　间：< font color=\"comment\"> 2021年12月25日 < /font >
            >每日一句：jitang+translation
            >[图片](https: // staticedu-wps.cache.iciba.com/image/d54b825982313e31a34efe6d51f851bd.png)'''

        },

        "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800
    })
    requests.post(sendUrl, data)


def getusersid(tocken):
    sendUrl = "https://qyapi.weixin.qq.com/cgi-bin/user/getuserid?access_token=" + tocken
    data = {"mobile": "16671048689"}
    requests.post(sendUrl, data=data)


if __name__ == "__main__":
    getTocken(id, secert, agentId)

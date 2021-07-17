from src.whether import get_time, get_content, get_weather
from src.poem import get_poem
import json
import requests
import sys
sys.path.append("D:\githubs\whut_spider")
id = "ww25c38dc950aba839"
secert = "IKnzzfncxbXSpmW25tvhMBhfgUvZ8j5F70LaxRiePtc"
agentId = "1000004"
time, count_down = get_time()
jitang, translation, image_url = get_content()
content = jitang+translation
day_weather, day_temperature, day_wind = get_weather()
weather = day_weather + day_temperature + day_wind


def getTocken(id, secert, agentId,kind):
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=" + id + "&corpsecret=" + secert
    r = requests.get(url)
    tocken_json = json.loads(r.text)
    if(kind == 1):  # 文本消息
        response = sendText(
            tocken=tocken_json['access_token'], agentId=agentId, msg=msg)
    elif(kind == 2):  # 图文消息
        response = article(tocken=tocken_json['access_token'], agentId=agentId)
    elif(kind == 3):  # 文本卡片消息
        response = textcard(
            tocken=tocken_json['access_token'], agentId=agentId)
    elif(kind == 4):  # markdown消息
        response = markdown(
            tocken=tocken_json['access_token'], agentId=agentId)
    return response.status_code


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
    bingurl = "https://api.fczbl.vip/bing/"
    text = get_poem()
    # print(sendUrl)
    data = json.dumps({
        "touser": "@all",
        "msgtype": "news",
        "agentid": agentId,
        "news": {
            "articles": [
                {
                    "title": "古诗词",
                    "description": text,
                    "url": "https://kwwgoo.github.io/",
                    "picurl": bingurl
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
        "agentid": agentId,
        "markdown": {
            "content":
            '''
            `考研倒计时`
            >今天是：< font color=\"warning\"> {time} < /font >
            >离考研还有:< font color=\"info\"> {count_down}天 < /font >
            >参与者：@ 韩玺廷、@ 邓永禧、@ 汪凯伟
            >时　间：< font color=\"comment\"> 2021年12月25日 < /font >

            >每日一句祝你心情美美哒:
            >{content}
            >[图片]({image_url})

            >下面为您播报武汉今日天气状况
            >{weather}
            '''.format(time=time, count_down=count_down, content=content, image_url=image_url, weather=weather)

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
    getTocken(id, secert, agentId,2)

import requests
import json
from whether import get_time, get_content, get_weather
import hashlib,base64
from urllib import request
from poem import get_poem

time, count_down = get_time()
jitang, translation, image_url = get_content()
content = jitang+translation
day_weather, day_temperature, day_wind = get_weather()
weather = day_weather + day_temperature + day_wind
text= get_poem()
bingurl = "https://api.fczbl.vip/bing/"
name = '每日一句.'+"jpg"
path = "D:\githubs\whut_spider\image"
request.urlretrieve(image_url, r'{}\{}'.format(path, name))




with open("./image/每日一句.jpg","rb") as f:
    img = f.read()
    MD5=hashlib.md5(img).hexdigest()
    DATA = str(base64.b64encode(img).decode())

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Content-Type": "application/json",
}
data = json.dumps({

    "msgtype": "markdown",
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
            '''.format(time=time, count_down=count_down, content=content,image_url=image_url, weather=weather)

    }
})

data2 = json.dumps({
    "msgtype": "image",
    "image": {
        "base64": DATA,
        "md5": MD5,
    }
})
data3 = json.dumps({
    "msgtype": "news",
    "news": {
       "articles" : [
           {
               "title" : "古诗词",
               "description" : text,
               "url" : "https://kwwgoo.github.io/",
               "picurl" : bingurl
           }
        ]
    }
})
response = requests.post(url, headers=headers, data=data)


import requests
import json
from whether import get_time, get_content, get_weather
import hashlib
import base64
from urllib import request
from poem import get_poem
from push import botpush, weipush

time, count_down = get_time()
count_down = '距离考研还有{}天，你准备好了吗？'.format(count_down)
jitang, translation, image_url = get_content()
content = jitang+translation
day_weather, day_temperature, day_wind = get_weather()
weather = day_weather + day_temperature + day_wind
a = '下面为您播报今日武汉天气状况\n'
b = '每日一句祝你有一个好的心情\n'
text = "今天是"+time+'\n'+count_down + \
    "你今天努力了吗？时刻准备着吗？不要怕，坚持到最后的才是胜利者，前途是光明的，道路是曲折的是🎉🎉🎉\n\n" + a + weather + "\n"+b + content
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
            >< font color=\"info\"> {count_down}天 < /font >
            >参与者：@ 韩玺廷、@ 邓永禧、@ 汪凯伟
            >时　间：< font color=\"comment\"> 2021年12月25日 < /font >

            >每日一句祝你心情美美哒:
            >{content}
            >[图片]({image_url})

            >下面为您播报武汉今日天气状况
            >{weather}
            '''.format(time=time, count_down=count_down, content=content, image_url=image_url, weather=weather)

    }
})
data2 = json.dumps({
    "msgtype": "text",
    "text": {
        "content": text,
        }})

botpush(data)
weipush(data2)
print("考研提醒推送成功")


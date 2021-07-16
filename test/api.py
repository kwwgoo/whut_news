# 指定时间内的文章
import urllib
from urllib import request
import sys
import ssl
import json

host = 'https://ali-star-lucky.showapi.com'
path = '/star'
method = 'GET'
appcode = '9adef75c01f144baaf5e168411b62745'
querys = 'needMonth=0&needTomorrow=0&needWeek=0&needYear=0&star=tianxie'
bodys = {}
url = host + path + '?' + querys

request = urllib.request.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib.request.urlopen(request, context=ctx)
content = response.read()
data = json.loads(content)
print(type(data))
data = data['showapi_res_body']['day']
luckytext =  "幸运时间:"+data['lucky_time']+",幸运颜色:"+data['lucky_color']+",幸运数字:"+data['lucky_num']
print(luckytext)
love_txt = "爱情运势"+data['love_txt']
money_txt = "财富运势"+data['money_txt']
work_txt = "学习运势"+data['work_txt']
general_txt = "运势简评"+data['general_txt']
day_notice = "今日提醒"+data['day_notice']
content = general_txt+"\n"love_txt +"\n"+money_txt+"\n"+day_notice
print(content)
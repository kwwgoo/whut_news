import requests
from lxml import etree
import json
import pyttsx3
import datetime
import urllib
from urllib import request
import sys
import ssl

# 获取日期和倒计时
def get_time():
    a = datetime.datetime.now()  # 实施时间
    y = str(a.year)
    m = str(a.month)
    d = str(a.day)  # 转换为字符串，便于打印
    time = y + '年' + m + '月' + d + '日' 
    b = datetime.datetime(2021, 12, 25)  # 自己设置的考研时间
    count_down = (b - a).days  # k考研倒计时
    return time, count_down


# 获取武汉当日天气情况
def get_weather():
    url = 'http://www.weather.com.cn/weather/101200101.shtml'
    response = requests.get(url)
    response.encoding = 'utf-8'
    response = response.text  # 获取页面
    html = etree.HTML(response)
    day_weather = '天气状况：' + html.xpath('//*[@id="7d"]/ul/li[1]/p[1]/text()')[0] + '\n'  # 获取天气，白天的天气
    high = html.xpath('//*[@id="7d"]/ul/li[1]/p[2]/span/text()')
    low = html.xpath('//*[@id="7d"]/ul/li[1]/p[2]/i/text()')  # 获取对应的两个温度
    # 因为页面在晚上会有小变化，所以使用条件语句，来排除因变化引起的bug
    if high == []:
        day_temperature = '室外温度：' + low[0] + '\n'
    else:
        day_temperature = '室外温度：' + low[0].replace('℃', '') + '~' + high[0] + '℃\n'  # 获取温度
    # 获取两个风向
    wind_1 = html.xpath('//*[@id="7d"]/ul/li[1]/p[3]/em/span[1]/@title')
    wind_2 = html.xpath('//*[@id="7d"]/ul/li[1]/p[3]/em/span[2]/@title')
    # 因为有时候，会出现两个风向是同一个风向的情况，所以使用条件语句排除
    if wind_2 == []:
        wind = wind_1[0] + '\n'
    elif wind_1[0] == wind_2[0]:
        wind = wind_1[0] + '\n'
    else:
        wind = wind_1[0] + '转' + wind_2[0] + '\n'
    # 因为风级有时候会出现“<"，语音的时候会认为是爱心符号，所以使用替换，改为文字”低于“
    wind_3 = html.xpath('//*[@id="7d"]/ul/li[1]/p[3]/i/text()')[0].replace('<', '低于').replace('>', '高于')
    day_wind = '风向情况：' + wind + wind_3 + '\n'  # 获取风向及风级
    return day_weather, day_temperature, day_wind


# 获取每日鸡汤
def get_content():
    url = 'http://open.iciba.com/dsapi/'  # 网上找的API
    response = requests.get(url=url)
    json_s = json.loads(response.text)
    jitang = json_s.get("content") + '\n'  # 每日鸡汤
    translation = json_s.get("note") + '\n'  # 中文翻译
    image_url = json_s.get("fenxiang_img")  # 图片链接
    return jitang, translation, image_url

def get_yunshi():
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
    content = general_txt+"\n"+love_txt +"\n"+money_txt+"\n"+day_notice
    print(content)
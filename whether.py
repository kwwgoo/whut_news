import requests
from lxml import etree
import json
import pyttsx3
import datetime
from push import push

# 获取日期和倒计时
def get_time():
    a = datetime.datetime.now()  # 实施时间
    y = str(a.year)
    m = str(a.month)
    d = str(a.day)  # 转换为字符串，便于打印
    time = y + '年' + m + '月' + d + '日' + '\n'
    b = datetime.datetime(2021, 12, 25)  # 自己设置的高考时间
    count_down = (b - a).days  # 高考倒计时
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


def main():
    time, count_down = get_time()
    day_weather, day_temperature, day_wind = get_weather()
    jitang, translation, image_url = get_content()
    count_down = '距离考研还有{}天，你准备好了吗？'.format(count_down) + "加油,相信你可以的"+'\n\n'
    a = '下面为您播报武汉今日天气状况\n'
    b = '每日一句，祝你心情美美哒:\n'
    time = '今天是' + time
    weather = day_weather + day_temperature + day_wind
    content = jitang + translation
    text = time + count_down + a + weather + b + content  # 语音内容
    print(text)
    with open("./notes.txt",'w') as f:
        f.write(text)
    push(text)


if __name__ == "__main__":
    main()

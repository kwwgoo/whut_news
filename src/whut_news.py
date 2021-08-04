import requests
import re
import os
from bs4 import BeautifulSoup
import datetime
from push import weipush
import json
# 爬取的页面
data = ""
# 推送内容
notions = []
# 推送标志位
flag = 1

# 爬取教务处公告


def spider():
    global data
    url = 'http://jwc.whut.edu.cn/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
    }
    response = requests.get(url, headers=headers)
    data = response.text


# 解析html获取教务处公告
def soup(data):
    global notions
    global flag
    # 正则匹配 用于提取教务处公告
    ex = "【教务处】.*?"
    soup = BeautifulSoup(data, "lxml")
    a_list = soup.select(".news-list li a")
    for a in a_list:
        if(re.match(ex, a.h6.string, re.S)):
            i = datetime.datetime.now()
            nowtime = str(datetime.datetime.today().date())
            time = a.span.string
            if(nowtime != time):
                flag = 0
                print("教务处无新公告，不进行推送")
            break
    with open("./notions.md", "w", encoding="utf-8") as f2:
        for a in a_list:
            if(re.match(ex, a.h6.string, re.S)):
                i = datetime.datetime.now()
                nowtime = str(datetime.datetime.today().date())
                time = a.span.string
                content = a.h6.string
                url = a['href']
                notion = "⏰"+time+"\n\n🎉"+content+"\n\n🏠"+url+"\n"
                notions.append(notion)
                f2.write("\n"+notion+"--------------------------------\n")


# 推送最新一条公告
if __name__ == "__main__":
    spider()
    soup(data)
    if(flag == 1):
        notion = "⭕教务处又有新通知啦" + \
            notions[0]+"\n💂[源码地址](https://github.com/kwwgoo/whut_news)"
        data = json.dumps({
            "msgtype": "text",
            "text": {
                "content": notion
            }
        })

        print("推送成功")
        weipush(data)
        Qsmgpush(notion)

import requests
import json
from fake_useragent import UserAgent
from push import botpush, weipush


def get_poem():
    global data
    url = 'https://v2.jinrishici.com/sentence'
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "X-User-Token": "/PYtLTGL588sGuMcFlZX4nQaP5MfIwIB",
    }
    response = requests.get(url, headers=headers)
    data = response.json()['data']['origin']
    title = data['title']
    dynasty = data['dynasty']
    author = data['author']
    contents = data['content']
    text = "《"+title+"》"+'\n'+"作者·"+dynasty+"·"+author+'\n'
    #print("  《"+title+"》"+'\n'+"    作者·"+dynasty+"·"+author)
    for content in contents:
        text += content+"\n"
    with open("./poem.txt", "a") as f:
        f.write(text)
    return text


if __name__ == "__main__":
    text = get_poem()
    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=56902235-478e-4fe4-8cab-a64e5776b81f'

    bingurl = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
    bingurl  = requests.get(bingurl).json()
    bingurl = "http://s.cn.bing.net"+bingurl['images'][0]['url']
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Content-Type": "application/json", }
    data = json.dumps({
        "msgtype": "news",
        "news": {
            "articles": [
                {
                    "title": "古诗词",
                    "description": text,
                    "url": "https://kwwgoo.github.io/",
                    "picurl": bingurl
                }
            ]
        }
    })
    #botpush(data)
    response=weipush(data)
    if(response.status_code==200):
        print("古诗词推送成功")

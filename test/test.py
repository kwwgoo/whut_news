import requests
from push import push
import json
from urllib import request


def get_content():
    url = 'http://open.iciba.com/dsapi/'  # 网上找的API
    response = requests.get(url=url)
    json_s = json.loads(response.text)
    jitang = json_s.get("content") + '\n'  # 每日鸡汤
    translation = json_s.get("note") + '\n'  # 中文翻译
    image_url = json_s.get("fenxiang_img")  # 图片链接
    print(image_url)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",}

    name = '每日一句.'+"jpg"
    path = "D:\githubs\whut_spider\image"
    request.urlretrieve(image_url, r'{}\{}'.format(path, name))
    with open("./image/每日一句.jpg","rb") as f:
        data=f.read()
     
    img = Image.open('./image/每日一句.jpg')
    print(img)

if __name__ == "__main__":
    get_content()

import requests
import json
from whether import get_content
import hashlib,base64
from urllib import request
from push import boturl

jitang, translation, image_url = get_content()
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
    "msgtype": "image",
    "image": {
        "base64": DATA,
        "md5": MD5,
    }
})
response_code = boturl(headers, data)
if (response_code == 200):
    print(每日一句图片推送成功)


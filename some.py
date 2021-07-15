import requests
import json
from fake_useragent import UserAgent
poems = ""
def get_poem():
    global data
    url = 'https://v2.jinrishici.com/sentence'
    headers ={
        "user-agent": str(UserAgent().random),
        "X-User-Token":"/PYtLTGL588sGuMcFlZX4nQaP5MfIwIB",
    }
    response = requests.get(url, headers=headers)
    data = response.json()['origin']
    title = data['title']
    dynasty = data['dynasty']
    author = data['author']
    content = data['content']
    print("《"+title+"》" +'\n' +content)


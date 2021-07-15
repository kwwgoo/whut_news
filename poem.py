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
    data = response.json()['data']['origin']
    title = data['title']
    dynasty = data['dynasty']
    author = data['author']
    contents = data['content']
    text =    "《"+title+"》"+'\n'+"作者·"+dynasty+"·"+author+'\n'
    #print("  《"+title+"》"+'\n'+"    作者·"+dynasty+"·"+author)
    for content in contents:
        text +=content+"\n" 

    print(text)
    push(text)
    with open("./poem","ab",encoding("utf-8")) as f:
        f.write(text)

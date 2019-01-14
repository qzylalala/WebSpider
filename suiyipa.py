import requests
import re
import os


url = 'http://huaban.com/boards/24116838/?md=newbn&beauty'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
response = requests.get(url, headers=headers).text
pattern = re.compile('"key":"(.*?)"', re.S)
items = re.findall(pattern, response)
os.mkdir('doubanya')
os.chdir('doubanya')
n = 0
for i in items:
    url = 'http://img.hb.aicdn.com/' + i
    r = requests.get(url, headers=headers)
    with open(str(n)+'.jpg', 'wb+') as f:
        f.write(r.content)
        print(n)
        n += 1
import requests
import re
from bs4 import BeautifulSoup
def get_url():
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    response = requests.get('https://www.zhihu.com/question/304197205/answer/543063634',headers = headers)
    info = response.text
    return info


soup = BeautifulSoup(get_url(), 'lxml')
with open('d:/1.txt', 'w', encoding='utf-8') as f:
    for i in soup.find_all(name='p'):
        f.write("{}".format(i.string))

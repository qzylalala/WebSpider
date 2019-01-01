import requests
from bs4 import BeautifulSoup
import re


def get_url():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    response = requests.get('https://weibo.com/u/2702384517?is_hot=1')
    info = response.text
    return info


sum = 0

soup = BeautifulSoup(get_url(), 'lxml')
#with open('d:/2.txt', 'w', encoding='utf-8') as f:
info = 
print(info)

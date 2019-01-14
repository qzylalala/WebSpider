import requests
from bs4 import BeautifulSoup
import json
import csv
import time



with open(r'美团武汉美食1.csv','w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'address'])
    for i in range(10):
        if i==0:
            continue
        url = 'http://wh.meituan.com/meishi/b1006/pn' + str(i) + '/'
        response = requests.get(url=url, headers={'User-Agent':''})
        soup = BeautifulSoup(response.text, 'lxml')
        info = soup.find_all('script')
        info = info[14].get_text().strip()
        info = info[19:-1]
        useful = json.loads(info)
        lists = useful['poiLists']['poiInfos']
        for j in lists:
            L = []
            L.append(j['title'])
            L.append(j['address'])
            writer.writerow(L)
        time.sleep(3)
        print('第' + str(i + 1) + '面')


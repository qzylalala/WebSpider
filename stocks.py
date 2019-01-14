import requests
from bs4 import BeautifulSoup
import csv


name = []
url = 'http://www.aastocks.com/tc/stocks/market/top-rank'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
info = soup.find_all(name='tr')[84:104]
for i in info:
    id = i.td.span.string
    name.append(id)
num = 0
info = soup.find_all(class_='cls txt_r pad3')
performance = []
caiwu = []
number = []
sum = []
yinglv = []
shizhanglv = []
shouyilv = []
money = []
for i in range(180):
    if i%9 == 1:
        performance.append(info[i].span.string)
    if i%9 == 2:
        caiwu.append(info[i].span.string)
    if i%9 == 3:
        number.append(info[i].string)
    if i%9 == 4:
        sum.append(info[i].string)
    if i%9 == 5:
        yinglv.append(info[i].string)
    if i%9 == 6:
        shizhanglv.append(info[i].string)
    if i%9 == 7:
        shouyilv.append(info[i].string)
    if i%9 == 8:
        money.append(info[i].string)
with open(r'股票.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['公司名', '股价变化', '股价升跌百分比', '成交量', '成交金额', '市盈率', '市财率', '收益率', '市值'])
    for i in range(20):
        Info = []
        Info.append(name[i])
        Info.append(performance[i])
        Info.append(caiwu[i])
        Info.append(number[i])
        Info.append(sum[i])
        Info.append(yinglv[i])
        Info.append(shizhanglv[i])
        Info.append(shouyilv[i])
        Info.append(money[i])
        writer.writerow(Info)
import  requests
from bs4 import BeautifulSoup


url = 'https://www.zhihu.com/question/275620469/answer/528408159'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
info = soup.find_all(class_='RichContent-inner')


with open('男神养成记.txt', 'w+') as f:
    for i in info[0].span.children:
        f.write(i.string + '\n')
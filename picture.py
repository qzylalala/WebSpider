from bs4 import BeautifulSoup
import requests
import os

def getHTML(url):
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    return response.text



def getINFO():
    list1 = []
    for i in range(1, 11):
        if i == 1:
            url = 'http://www.win4000.com/meinv167906.html'
        else:
            url = 'http://www.win4000.com/meinv167906_' + str(i) + '.html'
        soup = BeautifulSoup(getHTML(url), 'lxml')
        info = soup.find_all(id='pic-meinv')
        realinfo = info[0]
        list1.append(realinfo.a.img.attrs['data-original'])
    return list1

def savepic():
    info = getINFO()
    os.mkdir('folder')
    os.chdir('folder')
    for i in range (10):
        with open(str(i) + '.jpg', 'wb+') as f:
            pic = requests.get(info[i])
            f.write(pic.content)


if __name__ == "__main__":
    savepic()

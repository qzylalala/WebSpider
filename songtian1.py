import requests
from bs4 import BeautifulSoup
import bs4


url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'


def getHTMLText(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except:
        return ''


def filllist(ulist, url):
    soup = BeautifulSoup(url, 'lxml')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])


def printu(ulist, num):
    print("{:^10}\t{:^6}\t{:^10}\t{:^6}".format("排名", "学校", "省份", "总分"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}\t{:^6}".format(u[0], u[1], u[2], u[3]))


def main():
    uinfo = []
    html = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'
    url = getHTMLText(html)
    filllist(uinfo, url)
    printu(uinfo, 50)


main()


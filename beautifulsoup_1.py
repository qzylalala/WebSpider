html = """
'<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a''.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>' r'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>'
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.prettify())

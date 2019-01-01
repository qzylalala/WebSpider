html="""
<html>
<head>
<title>the dormousr's story</title>
</head>
<body>
<p class="story">
    once upon a time there were three little sisters;
    <a href="http://example.com/elsis" class="sister" id="link1">
<span>elsie</span>
</a>
<a href="http://example.com/lacie" class="sister" id="link2">lacie</a>
and
<a href="http://example.com/tillie" class"sister" id="link3">tillie</a>
and they lived at the bottom of a well.
</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
print(soup.p.contents)
from selenium import webdriver
import time


browser = webdriver.Chrome()
url = 'http://www.taobao.com'
browser.get(url)
print(browser.page_source)
time.sleep(10)
browser.close()
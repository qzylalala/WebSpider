from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from urllib.parse import quote


browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.google.com.hk/webhp?ie=UTF-8&gws_rd=cr&rct=j")
time.sleep(1)


input = browser.find_element_by_name('q')
input.send_keys('桃花期')
input.send_keys('\ue007')
time.sleep(5)
wait = WebDriverWait(browser, 10)
print(browser.page_source)
browser.close()

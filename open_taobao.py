from selenium import webdriver


browser = webdriver.Chrome()
browser.get("https://taobao.com")
print(browser.page_source)
browser.close()
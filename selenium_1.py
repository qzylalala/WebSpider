from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


browser = webdriver.Chrome()
try:
    browser.get('https://www.google.com.hk/webhp?ie=UTF-8&gws_rd=cr&rct=j')
    input = browser.find_element_by_name('q')
    input.send_keys('美女')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 50)
    wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()
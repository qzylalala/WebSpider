'''
from selenium import webdriver


browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/question/304197205/answer/543063634')
info = browser.find_elements_by_class_name('RichContent-inner')
'''



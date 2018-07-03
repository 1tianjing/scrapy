from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import requests
import time
driver = webdriver.Chrome(executable_path='/home/bc/桌面/chromedriver')

driver.get('https://www.zhaopin.com/')
time.sleep(5)
driver.find_element_by_id('KeyWord_kw2').send_keys('技术')
driver.find_element_by_class_name('doSearch').click()
time.sleep(5)
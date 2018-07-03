from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from lxml import etree

browse = webdriver.Chrome(executable_path='/home/bc/桌面/chromedriver')
browse.get('https://github.com/login')
browse.find_element_by_id('login_field').send_keys('tianjing2023@aliyun.com')
browse.find_element_by_id('password').send_keys('tianjing123456')
browse.find_element_by_xpath('.//input[@class="form-control form-control input-block"]').click()

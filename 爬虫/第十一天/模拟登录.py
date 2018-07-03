from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

browse = webdriver.Chrome(executable_path='/home/bc/桌面/chromedriver')
browse.get('https://www.douban.com/')
browse.find_element_by_id('form_email').send_keys('18550548720')
browse.find_element_by_id('form_password').send_keys('tianjing123')
browse.find_element_by_class_name('bn-submit').click()

# cookie_str = ''
# for cookir in browse.get_cookies():
#     cookie_str +=



















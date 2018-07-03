#导入webdriver  使用浏览器驱动
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browse = webdriver.Chrome(executable_path='/home/bc/桌面/chromedriver')

#模拟浏览器发起一个请求
browse.get('https://www.baidu.com')
#获取的是浏览器渲染之后的页面
print(browse.page_source)

#模拟用户输入
browse.find_element_by_id('kw').send_keys('王源')

time.sleep(5)

#模拟用户点击
browse.find_element_by_id('su').click()

time.sleep(5)

#模拟点击下一页
# browse.find_elements_by_class_name('n')[0].click() 获取所有的
# browse.find_element_by_class_name('n').click()
time.sleep(5)

#点击更多
browse.find_element_by_xpath('.//div[@class="s_tab"]/a[last()-1]').click()


# #获取网页页面(生成当前的页面快照并保存)
# driver.save_screenshot('baidu.png')
#
# #获取当前页面的cookies()
# cookies = driver.get_cookies()
# cookie = ''
# for item in cookies:
#     cookie += item['name']+item['value']+' ;'
# print(cookie[:-1])


time.sleep(5)
# #模拟前进
# browse.forward()
# #模拟后退
# browse.back()

time.sleep(5)
# 关闭所有
browse.close()
# 退出当前
browse.quit()
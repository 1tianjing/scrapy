from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from lxml import etree
import json

browse = webdriver.Chrome(executable_path='/home/bc/桌面/chromedriver')

#搜索淘宝美食
def search():
    #模拟浏览器发起一个请求
    browse.get('https://www.taobao.com/')
    #获取浏览器渲染以后的页面内容
    # print(browse.page_source)
    #模拟用户输入关键字
    browse.find_element_by_id('q').send_keys('美食')

    time.sleep(5)

    #模拟用户搜索按钮点击,获取商品列表页面源码
    browse.find_element_by_xpath('//div/button[@class="btn-search tb-bg"]').click()
    if browse.page_source:
        getprodect_items(browse.page_source)

def getprodect_items(html):
    response = etree.HTML(html)
    items = response.xpath("//div[@class='item J_MouserOnverReq']")
    for each in items:
        print(each)
        # print()
        # image_url、title、buynum、price、store、location
        print("------华丽的商品分割线-----")
        image_url = each.xpath('.//div[@class="dic"]/a/img/@src')[0]
        title = each.xpath('.//div[@class="J_ItemPic img"]/a/img/@alt')[0]
        price = each.xpath('.//div[@"price g_price g_price-highlight"]/strong/text()')[0]
        buynum = each.xpath('.//div[@class="deal-cnt"]/text()')[0]
        store = each.xpath('.//a[@class="shopname J_MouseEneterLeave J_ShopInfo"]/span[2]/text()')

        print("商品图片地址："+"https:"+image_url)
        print("商品名称:"+title)
        print("商品价格:"+price)
        print("购买数量:"+buynum)
        print("店铺名称:"+store)
        # 这里需要将数据写如数据库
        dict={
            '图片地址':image_url,
            '商品名称':title,
            '商品价格':price,
            '购买数量':buynum,
            '店铺名称':store
        }
        with open('taobao.json','a') as f:
            f.write(json.dumps(dict,ensure_ascii=False)+'\n')

    #获取下一页的数据
    time.sleep(5)
    #找到下一页的按钮,并点击获取下一页商品列表源码
    browse.find_element_by_css_selector("li.item.next a.J_Ajax.num.icon-tag").click()



    #如果数据存在就进行提取数据
    if browse.page_source:
        time.sleep(5)
        #递归方法获取数据
        getprodect_items(browse.page_source)


def main():
    search()
    # time.sleep(10)
    # #测试时,停留十秒后关闭浏览器
    # browse.quit()


if __name__ == '__main__':
    main()

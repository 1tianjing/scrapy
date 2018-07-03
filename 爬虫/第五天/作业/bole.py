from urllib.request import Request,urlopen
import re
import requests
from lxml import etree
import pymysql


def get(url,start,end):
    for page in range(start,end + 1):
        furl = url + 'page/%s/'%page  #链接+页码构成一个新的链接
        chuli(furl)
        print(furl)


def chuli(furl):
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }

    url = 'http://top.jobbole.com/'
    response = requests.get(url,headers=header)  #发起一个请求

    # print(response.text)
    page_html = etree.HTML(response.text)  #转换html
    list = page_html.xpath('//li[@class="media"]')  #先写一个范围
    for item in list:
        title = item.xpath('.//h3[@class="p-tit"]/a/text()')[0]  #标题
        link = item.xpath('.//h3[@class="p-tit"]/a/@href')[0]     #链接
        pub_data = item.xpath('.//p[@class="p-meta"]/span[1]/text()')[0]   #发布时间
        tag = item.xpath('.//p[@class="p-meat"]/span[@class="p-tags"]/a/text()')  #标签
        if len(tag) == 0:
            tag = '没有标签'
        #如果存在i[@class="fa fa-comments-o"]，说明有评论
        comment = item.xpath('.//i[@class="fa fa-comments-o"]')
        if len(comment) == 0:
            comment = '0'  #如果没找到i[@class="fa fa-comments-o"]，说明没有评论
        elif len(comment) > 0:
            if tag == '没有标签':   #有评论，没标签
                comment = item.xpath('.//p[@class="p-meta"]/span[2]/a/text()')[0]
            else:   #有评论  有标签
                comment = item.xpath('.//p[@class="p-meta"]/span[3]/a/text()')[0]
        print(title, link, pub_data,tag,comment)
        # 连接数据库
        conn = pymysql.connect(host='127.0.0.1', user='root', password='bc123', database='bole', port=3306,charset='utf8')
        cur = conn.cursor()
        sql = 'INSERT INTO bole(title, link, pub_data,tag,comment) VALUES("%s","%s","%s","%s","%s")'
        cur.execute(sql,(title, link, pub_data,tag,comment))
        conn.commit()
        conn.close()


def fenye():
    fenye = int(input('请输入查询的页数：'))
    q = ( fenye - 1)*15
    conn = pymysql.connect(host='127.0.0.1', user='root', password='bc123', database='bole', port=3306,charset='utf8')
    cur = conn.cursor()
    sql = 'select * from bole limit %d,15'%int(q)
    cur.execute(sql)
    result = cur.fetchall()
    print(result)
    conn.commit()
    conn.close()
fenye()
if __name__ == '__main__':
    start = int(input("请输入开始的页数："))
    end = int(input("请输入截止的页数："))
    url = 'http://top.jobbole.com/'
    #http://top.jobbole.com/page/2/
    get(url,start,end)

    



# <li class="media">
# <a id="38654voteflag" title="顶起，让更多人看到" alt="顶起，让更多人看到" class="href-style p-cnt  vote-post-up  register-user-only " data-post-id="38654" data-current-vote="1">
# <span id="38654votetotal">27</span>
# <i class="fa fa-chevron-up"></i>
# </a>

# <div class="media-body">
# <h3 class="p-tit">
# <a target="_blank" href="http://top.jobbole.com/38654/">地址 1.1.1.1，Cloudflare 推新公共 DNS 服务</a>
# <label class="hide-on-480 small-domain-url"></label>
# </h3>
# <p class="p-meta">
# <span>04/02</span>
# <span>
# <a href="http://top.jobbole.com/38654/#comments">
# <i class="fa fa-comments-o"></i> 5 </a>
# </span>
# </p>
# </div>
# </li>








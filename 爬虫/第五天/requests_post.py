#post请求
import requests
#拉勾网
#目标url  https://www.lagou.com/jobs/companyAjax.json?needAddtionalResult=false
url = 'https://www.lagou.com/jobs/companyAjax.json?needAddtionalResult=false'

data = {
    'first':'false',
    'kd':'python',
    'pn':'1'
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'cookie':'JSESSIONID=ABAAABAACEBACDGB80E621D79CC24FCC01B8AD00334F10A; __guid=237742470.3812041392653456000.1528251162078.238; user_trace_token=20180606101215-081bccf5-692f-11e8-9238-525400f775ce; PRE_UTM=m_cf_cpt_360_pc; PRE_HOST=www.so.com; PRE_SITE=https%3A%2F%2Fwww.so.com%2Fs%3Fie%3Dutf-8%26src%3D360se7_addr%26q%3Dlagou; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F%3Futm_source%3Dm_cf_cpt_360_pc; LGUID=20180606101215-081bd011-692f-11e8-9238-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_navigation; _gid=GA1.2.607189201.1528251163; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528251163,1528251174; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528252405; _ga=GA1.2.67963731.1528251163; LGSID=20180606101215-081bce8e-692f-11e8-9238-525400f775ce; LGRID=20180606103310-f469ff25-6931-11e8-923e-525400f775ce; SEARCH_ID=c3e02e7c941e4d768547da6127d33127; monitor_count=9',
    'Referer':'https://www.lagou.com/zhaopin/Python/2/?filterOption=3',
    'Host':'www.lagou.com',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate, br',
    'Connection':'keep-alive',
    'Content-Length':'25',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Anit-Forge-Token':'None',
    'X-Requested-With':'XMLHttpRequest'
}

response = requests.post(url,data=data,headers=headers)
response.encoding = 'utf-8'
# print(response.text)
print(response.status_code)
#使用json()
data = response.json()
print(data['content'])
print(type(data))

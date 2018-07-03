import requests
import threading
import json
from lxml import etree
import queue

# 找到ajax接口 
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=20289457&count=15&category=-1

response = requests.get('https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=20289457&count=15&category=-1')

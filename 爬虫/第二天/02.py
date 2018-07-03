from urllib.request import Request,urlopen
import urllib.parse as parse
import re

html = """
<div class="sb">
<a class="sb2" src="https://www.ugirls.com/Index/Search/Magazine-57-3.html">哈哈哈</a>
</div>
"""

pattern = re.compile('<div.*?sb.*?sb2.*?src="(.*?)">(.*?)</a>',re.S)
result=re.findall(pattern,html)
print(result)
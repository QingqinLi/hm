"""

"""
import re
from urllib.request import urlopen
import requests

# # res = urlopen("https://movie.douban.com/top250?start=1&filter=")
# res = requests.get("https://movie.douban.com/", verify=False)
# # print(res.content.decode('utf-8'))
# # print(res.url)
#
# com = re.compile(r'<li class="ui-slide-item"  data-title=.*? data-release="20', re.S)
#
#
# ret = com.findall(res.content.decode('utf-8'))
# # print(ret)
# lst = []
# for i in ret:
#     lst.append(i.replace('<li class="ui-slide-item"  data-title="', "").replace('" data-release="20', ""))
# print(lst)


res = requests.get('')
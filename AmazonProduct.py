# -*- coding: utf-8 -*-
# @Author: cui
# @Date:   2018-03-29 14:50:28
# @Last Modified by:   cui
# @Last Modified time: 2018-03-29 14:52:32

import requests
url = "https://www.amazon.cn/dp/B01M8L5Z3Y/"
try:
  kv = {'user-agent': 'Mozilla/5.0'}
  r = requests.get(url, headers=kv)
  r.raise_for_status()
  r.encoding = r.apparent_encoding
  print(r.text[1000:2000])
except:
  print("爬取失败")
# -*- coding: utf-8 -*-
# @Author: cui
# @Date:   2018-03-29 15:00:42
# @Last Modified by:   cui
# @Last Modified time: 2018-03-29 15:01:52

import requests
url = "https://item.jd.com/5181380.html"
try:
  r = requests.get(url)
  r.raise_for_status()
  r.encoding = r.apparent_encoding
  print(r.text[:1000])
except:
  print("爬取失败")
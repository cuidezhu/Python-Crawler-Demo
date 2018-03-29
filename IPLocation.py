# -*- coding: utf-8 -*-
# @Author: cui
# @Date:   2018-03-29 15:03:00
# @Last Modified by:   cui
# @Last Modified time: 2018-03-29 15:16:10

import requests
url = "http://www.ip138.com/ips138.asp?ip="
try:
  r = requests.get(url + '202.204.80.112')
  r.raise_for_status()
  r.encoding = r.apparent_encoding
  print(r.text[7000:8000])
except:
  print("爬取失败")
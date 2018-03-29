# -*- coding: utf-8 -*-
# @Author: cui
# @Date:   2018-03-29 14:46:23
# @Last Modified by:   cui
# @Last Modified time: 2018-03-29 14:48:04
import requests
keyword = "Python"
try:
  kv = {'q':keyword}
  r = requests.get("http://www.so.com/s", params=kv)
  print(r.request.url)
  r.raise_for_status()
  print(len(r.text))
except:
  print("爬取失败")
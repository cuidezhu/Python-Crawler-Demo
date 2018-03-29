# -*- coding: utf-8 -*-
# @Author: cui
# @Date:   2018-03-29 14:39:55
# @Last Modified by:   cui
# @Last Modified time: 2018-03-29 14:44:01
import requests
keyword = "Python"
try:
  kv = {'wd': keyword}
  r = requests.get("http://www.baidu.com/s", params=kv)
  print(r.request.url)
  r.raise_for_status()
  print(len(r.text))
except:
  print("爬取失败")

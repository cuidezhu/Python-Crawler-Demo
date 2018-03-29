# -*- coding: utf-8 -*-
# @Author: cui
# @Date:   2018-03-29 14:26:56
# @Last Modified by:   cui
# @Last Modified time: 2018-03-29 14:35:12

import requests
import os
url = "http://image.nationalgeographic.com.cn/2018/0314/20180314015318819.jpg"
root = "/Users/cui/Desktop/"
path = root + url.split('/')[-1]
try:
  if not os.path.exists(root):
    os.mkdir(root)
  if not os.path.exists(path):
    r = requests.get(url)
    with open(path, 'wb') as f:
      f.write(r.content)
      f.close()
      print("文件保存成功")
  else:
    print("文件已存在")
except:
  print("爬取失败")
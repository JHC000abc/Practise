#!/usr/bin/env python
# encoding: utf-8
'''
@author: JHC
@license: None
@contact: JHC000abc@gmail.com
@file: test.py
@time: 2022/1/25 9:54
@desc:
'''

import requests
import base64

# API地址
url = "http://192.168.0.115:5000/photo"
# 图片地址
file_path = r'./11.jpg'
file_path1 = r'./1.jpg'
# 图片名
file_name = file_path.split('/')[-1]
file_name1 = file_path1.split('/')[-1]
# 二进制打开图片
file = open(file_path, 'rb')
file1 = open(file_path1, 'rb')
# 拼接参数
files = {'front': (file_name, file, 'image/jpg'),
         'back': (file_name1, file1, 'image/jpg'),
         }
data = {'scan_num':12222}

# 发送post请求到服务器端
print(files)
print(data)
r = requests.post(url, files=files,data=data)
# 获取服务器返回的图片，字节流返回
# result = r.content
# 字节转换成图片
# img = base64.b64decode(result)
# file = open('test1.jpg', 'wb')
# file.write(img)

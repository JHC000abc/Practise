#!/usr/bin/env python
# encoding: utf-8
'''
@author: JHC
@license: None
@contact: JHC000abc@gmail.com
@file: te.py
@time: 2022/1/17 14:28
@desc:
'''
import json

import requests
url = 'http://192.168.0.115:5000/login'
data = {
'native_code':"manageserver-001",
'username':111,
         'password':111
}
print(type(data))
print(str(data))
# data2 = str(data)
data = json.dumps(data)


print(data)
print(type(data))
data={'data':data}
print(data)
response = requests.post(url,data)
print(response)
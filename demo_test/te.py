#!/usr/bin/env python
# encoding: utf-8
'''
@author: JHC
@license: None
@contact: JHC000abc@gmail.com
@file: te.py
@time: 2022/1/29 16:24
@desc:
'''
import base64
import json

import requests


url = 'http://192.168.0.115:9999/get/pic'
data_dict = {}
with open(r"C:\Users\JHC\Desktop\majorcontrol\majorcontrol\storage\pic\1022745_w_MC20210901-002_0.bmp",
          "rb") as front_data:
    front_data = front_data.read()  # 图片：二进制格式
    front_data_bytes = base64.b64encode(front_data)  # 二进制格式 ---> bytes类型
    front_data_str = front_data_bytes.decode()  # base64格式 ---> str类型
    print(1111, type(front_data_str))
    data_dict['front'] = front_data_str

with open(r"C:\Users\JHC\Desktop\majorcontrol\majorcontrol\storage\pic\1022746_m_MC20210901-002_1.bmp", "rb") as above_data:
                above_data = above_data.read()  # 图片：二进制格式
                above_data_bytes = base64.b64encode(above_data)  # 二进制格式 ---> bytes类型
                above_data_str = above_data_bytes.decode()  # base64格式 ---> str类型
                print(22222, type(above_data_str))
                data_dict['back'] = above_data_str

with open("./device_info.json", "r") as data:
                data = data.read()
                data = json.loads(data)
                data_dict["scan_total_num"] = data["scan_total_num"]

data1 = json.dumps(data_dict)

res = requests.post(url,data={"data":data1})
print(res.text)

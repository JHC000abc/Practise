#!/usr/bin/env python
# encoding: utf-8
'''
@author: JHC
@license: None
@contact: JHC000abc@gmail.com
@file: tt3.py
@time: 2022/1/25 14:41
@desc:
'''

# 判图后的位置信息 OK
@app_.route('/scan/location', methods=["POST", "GET"])
def scan_location():
    if request.method == "POST":
        data_dict = {}
        # 12.json就是位置信息的文件
        with open(r"./12.json", encoding="utf8") as location_data:
            # print(type(location_data))
            data_dict['location_information'] = location_data.read()
        data = json.dumps(data_dict)
        return data
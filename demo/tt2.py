#!/usr/bin/env python
# encoding: utf-8
'''
@author: JHC
@license: None
@contact: JHC000abc@gmail.com
@file: tt2.py
@time: 2022/1/25 13:15
@desc:
'''
def test_heart4():
    url = "http://" + ip + ":8888" + "/heart"
    device_info = {}
    device_info["login_time"] = "2022/1/7 8:30:00"
    device_info["login_user"] = "user04"
    device_info["login_gender"] = "man"
    device_info["scan_model"] = "artificial mode"
    device_info["scan_num"] = 88
    device_info["scan_total_hour"] = 38456
    device_info["scan_total_num"] = 1888
    device_info["type"] = "judge"
    device_info["work_model"] = "target mode"
    device_info["warning_json_msg"] = '{\\n \\"native_code\\": \\"major-039\\",\\n \\"warning_msg\\": \\"\\\\u8fd1\\\\u7aef\\\\u8bbe\\\\u5907\\\\u65ad\\\\u5f00\\\\u8fde\\\\u63a5\\",\\n \\"warning_time\\": \\"2021-12-12 12:12:12\\"\\n}'
    data = {"data": json.dumps(device_info, ensure_ascii=False)}
    ret = requests.post(url, data=data)
    print(ret.text)
#!/usr/bin/env python
# encoding: utf-8
'''
@author: JHC
@license: None
@contact: JHC000abc@gmail.com
@file: te'.py
@time: 2022/2/14 16:02
@desc:
'''

alarmParam = [{
		"id": "00001",
		"position": [
			208,
			536,
			274,
			564
		]
	},
	{
		"id": "00002",
		"position": [
			142,
			550,
			172,
			600
		]
	}
]
position = [i["position"] for i in alarmParam]
print(position)
b = 536
a = [208, 536, 274, 564]
print(a.index(b))


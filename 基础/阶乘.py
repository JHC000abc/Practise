#!/usr/bin/env python
# encoding: utf-8
'''
@author: JHC
@license: None
@contact: JHC000abc@gmail.com
@file: 阶乘.py
@time: 2022/1/13 20:59
@desc:
'''

def jiecheng(num):
    sum = 1
    if num == 0:
        print(1)
        return 1
    else:
        for i in range(1,num+1):
            # print(i)
            sum *= i
        print('{}阶乘结果为:{}'.format(num,sum))


jiecheng(10)
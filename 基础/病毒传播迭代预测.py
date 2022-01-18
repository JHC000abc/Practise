#!/usr/bin/env python
# encoding: utf-8
'''
@author: JHC
@license: None
@contact: JHC000abc@gmail.com
@file: 病毒传播迭代预测.py
@time: 2022/1/13 21:15
@desc:
'''
import math



def infect_num_count(date):
    # if date <= 5:
    #     print('第{}天,病毒传播了{}代，感染人数为{}'.format(date, 0, 1))
    # else:
    iter_num = math.ceil(date/5)
    # print('病毒传播:{}代'.format(iter_num-1))
    for i in range(iter_num):
        infect_num = 2**i
        # print(infect_num)
    print('第{}天,病毒传播了{}代，感染人数为{}'.format(date,iter_num,infect_num))


infect_num_count(date=24)
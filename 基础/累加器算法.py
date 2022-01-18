#!/usr/bin/env python
# encoding: utf-8
'''
@author: JHC
@license: None
@contact: JHC000abc@gmail.com
@file: 累加器算法.py
@time: 2022/1/13 20:10
@desc:
'''
import time


def add(num):
    sum = 0
    for i in range(1,num+1):
        sum += i
    print('累加结果为:{}'.format(sum))

time_start = time.process_time()
add(100000)
time_end = time.process_time()
print('执行耗时:{}'.format(time_end - time_start))


def add_optimize(num):
    sum = num*(1+num)/2
    print('累加结果为:{}'.format(sum))


time_start_1 = time.process_time()
add_optimize(100000)
time_end_1 = time.process_time()
print('执行耗时:{}'.format(time_end_1 - time_start_1))

"""
算法时间复杂度：常数阶(1) < 对数阶(log(n)) < n < nlog(n) (前边高效算法，后边低效算法)< n^2 < 2^n < n!
"""

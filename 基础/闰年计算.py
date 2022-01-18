#!/usr/bin/env python
# encoding: utf-8
'''
@author: JHC
@license: None
@contact: JHC000abc@gmail.com
@file: 闰年计算.py
@time: 2022/1/14 19:22
@desc:
'''


def run_year(year):
    if year > 0:
        if year % 4 == 0 and year % 100 != 0:
            print('{}年是润年'.format(year))
        elif year % 400 == 0:
            print('{}年是润年'.format(year))
        else:
            print('{}年不是润年'.format(year))
    else:
        print('请输入公元后年份!!!')


run_year(2020)
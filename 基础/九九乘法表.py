#!/usr/bin/env python
# encoding: utf-8
'''
@author: JHC
@license: None
@contact: JHC000abc@gmail.com
@file: 九九乘法表.py
@time: 2022/1/13 19:54
@desc:
'''

for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(j,i,i*j),end=' ')
    print('\n')


date = [['{}*{}={}'.format(j,i,i*j)for i in range(1,10)]for j in range(1,i+1)]
print(date)

#!/usr/bin/env python
# encoding: utf-8
'''
@author: JHC
@license: None
@contact: JHC000abc@gmail.com
@file: 抽纸牌.py
@time: 2022/1/13 20:29
@desc: 生成一副纸牌（54张）,俩人随机抽取3张
'''

import random


card_suit_list = ['红桃','梅花','方块','黑桃']
card_num_list = ['A']+[i for i in range(2,11)]+['J','O','K']
# print(card_num_list)
card = [i+str(j) for j in card_num_list for i in card_suit_list]+['大王','小王']
# print(card)
# print(len(card))

show_list1 = random.sample(card,3)
show_list2 = random.sample(card,3)

print(show_list1,'\n',show_list2)

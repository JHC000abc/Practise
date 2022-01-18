# import datetime
#
# # 给定要增加的小时数,计算当前时间加上增加小时数后的日期
# def sum_time(hours):
#     now = datetime.datetime.now()
#     print('当前时间:', str(now).split('.')[0])
#
#     date = now - datetime.timedelta(hours=hours)
#     print('计算后时间:', str(date).split('.')[0])
#
#
#
# hours = input('请输入要添加的小时数:')
# hours=int(hours)
# sum_time(hours)
#
# # 给定要增加的星期数,计算当前时间加上增加星期数后的日期
# def sum_time(weeks):
#     now = datetime.datetime.now()
#     print('当前时间:', str(now).split('.')[0])
#     print(datetime.date.today())
#     print(type(now))
#
#     date = now + datetime.timedelta(weeks=weeks)
#     print('计算后时间:', str(date).split('.')[0])
#
#
#
# weeks = input('请输入要添加的星期数:')
# weeks=int(weeks)
# sum_time(weeks)
# import datetime
#
# time = datetime.date(2021,12,11)
# print(time)
# print(type(time))
# import datetime
# print(datetime.datetime.now())
# import datetime
# import time
#
#
# def time_differ(date1='15:00',date2='13:15:05'):
#
#      date1=datetime.datetime.strptime(date1,"%Y-%m-%d %H:%M:%S")
#      date2=datetime.datetime.strptime(date2,"%Y-%m-%d %H:%M:%S")
#      return date2-date1
#
# date1 = str(datetime.datetime.now()).split('.')[0]
# while True:
#     date2 = str(datetime.datetime.now()).split('.')[0]
#     differ = time_differ(date1,date2)
#     time.sleep(1)
#
#     print(differ)

import json

lis = {'birthday': '2021-12-12 12:12:12', 'canuse': 'True', 'email': '123@sadad.com', 'gender': '男', 'id': 1, 'idcard': '1232da1312313123', 'password': '', 'phone': '23131dsa23131', 'privilege': '00000000', 'relname': '掌门2', 'username': '', 'usertype': '维修员', 'workid': '132131313'}
lis2 = {'birthday': '2021-12-12 12:12:12', 'canuse': 'True', 'email': '123@sadad.com', 'gender': '男', 'id': 1, 'idcard': '1232da1312313123', 'password': '', 'phone': '23131dsa23131', 'privilege': '00000000', 'relname': '掌门2', 'username': '', 'usertype': '维修员', 'workid': '111111'}
print(type(lis2))
date = [lis2,lis]
print(date)
data = json.dumps(date)
print(data)
print(type(data))
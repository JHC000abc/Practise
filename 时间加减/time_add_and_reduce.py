import datetime

# 给定要增加的小时数,计算当前时间加上增加小时数后的日期
def sum_time(hours):
    now = datetime.datetime.now()
    print('当前时间:', str(now).split('.')[0])

    date = now + datetime.timedelta(hours=hours)
    print('计算后时间:', str(date).split('.')[0])



hours = input('请输入要添加的小时数:')
hours=int(hours)
sum_time(hours)

# 给定要增加的星期数,计算当前时间加上增加星期数后的日期
def sum_time(weeks):
    now = datetime.datetime.now()
    print('当前时间:', str(now).split('.')[0])

    date = now + datetime.timedelta(weeks=weeks)
    print('计算后时间:', str(date).split('.')[0])



weeks = input('请输入要添加的星期数:')
weeks=int(weeks)
sum_time(weeks)
import numpy as np
from scipy import stats
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt


'''
https://www.cjavapy.com/article/1146/
'''
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# 平均数
print('平均数:',np.mean(speed))

# 中位数
print('中位数:',np.median(speed))

# 众数
print('众数：',stats.mode(speed).mode[0])
print('众数出现次数：',stats.mode(speed).count[0])

# 统计词频
print(pd.value_counts(speed))
print(dict(Counter(speed)))

# 通过词频统计 计算众数
print('众数：',pd.value_counts(speed).keys()[0])

# 标准差
print('标准差：',np.std(speed))

# 方差 每个值和平均值的差值的平方的和的平均值
print('方差：',np.var(speed))

# 百分位数 （打印的值为87） 50%的速度是87以下
print('百分位数：',np.percentile(speed,50))

# 取-100.0 到 5.0 之间的250个随机数创建数组
print(np.random.uniform(-100.0,5.0,250))
# 取1，101 之间的22个随机数创建数组
print(np.random.randint(1,101,22))

# 直方图 hist
data = np.random.uniform(-1,1,10)
# data = np.random.randint(-10,10,100)
print(data)
print(pd.value_counts(data))
plt.hist(data,10)
# plt.show()

# 正态数据分布 (平均值，标准差)
data2 = np.random.normal(5.0,1.0,100000)
print('data2=',data2)
plt.hist(data2,100)
# plt.show()

# 散点 scatter
x = np.random.randint(1,10,100)
y = np.random.randint(1,10001,100)
plt.scatter(x,y)
plt.show()

# 回归


import pandas as pd
import numpy as np
from scipy import stats
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from scipy import stats

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
# plt.show()

# 回归 scipy r为相关关系，范围是0（没关系）到1（100%相关）
x = [1,2,3,4,5,6,7,8,9,10]
y = [20,30,40,50,60,70,80,90,100,110]
slope,intercept,r,p,std_err = stats.linregress(x,y)
def myfun(x):
    return slope * x + intercept
mymodel = list(map(myfun,x))
# 散点
plt.scatter(x,y)
# 线性回归线
plt.plot(x,mymodel)
# plt.show()
print('r=',r)
# 预测未来
speed = myfun(100)
print(speed)

# 多项式回归
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
mymodel2 = np.poly1d(np.polyfit(x,y,3))
myline = np.linspace(1,22,100)
# 画散点
plt.scatter(x,y)
# 画回归线
plt.plot(myline,mymodel2(myline))
# plt.show()
print('mymodel2=',mymodel2)
print('mymodel2(myline)=',mymodel2(myline))
# 多项式回归拟合度计算(0.94 表示拟合度很好)
from sklearn.metrics import r2_score
print(r2_score(y,mymodel2(x)))
# 预测未来
speed = mymodel2(20)
print(speed)

# 多元回归
df = pd.read_csv('./data/ok.csv')
print(df)
# 独立值
X = df[['Weight','Volume']]
print(X)
# 相关值
y = df['CO2']
print(y)
from sklearn import linear_model
regr = linear_model.LinearRegression()
# print(regr)
regr.fit(X, y)
print('regr.coef_=',regr.coef_)
# 输出预测值
predictedCO2 = regr.predict([[3300, 1300]])
print(predictedCO2)

# 数据归一化


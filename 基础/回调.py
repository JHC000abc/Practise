# def huidiao(f):
#     f()
#
# def love():
#     print(123)
#
#
# huidiao(love)

def qiuhe(x,y,fu):
    print(fu(x,y))

qiuhe(2,5,pow)


x=lambda x,y:pow(x,y)
print(x(2,4))

y=lambda sex:'男'if sex==1 else '女'
print(y(0))



a=lambda age : '张三' if age>12 else '里斯'
print(a(11))
print(a(18))
print('1'.isdecimal(),'wiof')





n=lambda x:x*x
print(n(2))


m=lambda x,y:'相同' if x==y else '不同'
print(m('\\1','\1'))


# 判断两个字符串是否相同

o=lambda x,y:'相同' if len(str(x))==1 and len(str(y))==1 and ord(str(x))==ord(str(y)) else '不同'
print(o('[1]','[1]'))






from functools import reduce
def qww(q,p):
    print(reduce(lambda x, y: True if x == y else False, (str(q),str(p))))

qww(1,11)


# import numpy as np
# x_list = np.random.randint(1,10,130)
# y_list = np.random.randint(1,10,130)
# for i in range(len(x_list)):
#     print('x_list[i]={},y_list[i]={}'.format(x_list[i],y_list[i]))
#     qww(x_list[i],y_list[i])


# def qww(x,y):
#     if x==y:
#         return True
#     else:
#         return False
#
#
# print(qww(1, 1))
qww = lambda x,y :True if x==y else False

print(qww(1,1))
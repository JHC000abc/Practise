def jiecheng(num,result):
    if num>1:
        result = num*result
        num-=1
        jiecheng(num,result)

    else:
        print('result=', result)

# jiecheng(5, 1)


def jiecheng1_1(num):
    if num==1:
        return 1
    else:
        return num*jiecheng1_1(num-1)

# print(jiecheng1_1(5))

def jiecheng2(num):
    result=1
    for i in range(1,num+1):
        result*=i
    print('result=',result)

# jiecheng2(5)

from functools import reduce
def jiecheng3(num):
    result = reduce(lambda x,y:x*y,range(1,num+1))
    print(result)

# jiecheng3(5)




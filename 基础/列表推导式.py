list = [[1,2,3],
        [4,5,6],
        [7,8,9]
]

new_list=[]
for i in range(3):
    lis = []
    for j in list:
        lis.append(j[i])
    new_list.append(lis)
print(new_list)

new_list2=[[[j[i]]for j in list]for i in range(3)]
print(new_list2)




for i in range(1,10):
    print(' ')
    for j in range(i,10):
        print('{}*{}={}'.format(i,j,i*j),end=' \n')
print('\n\n')
b=[['{}*{}={}'.format(i,j,i*j) for j in range(i,10)]for i in range(1,10)]
print(b)



dict = {
    'user':'admin',
    'age':23,
    'phone':'137'
}
list=[]
print(len(dict))
for i in dict:
    # print(i)
    list.append('{}={}'.format(i,dict[i]))
print(list)

c=[i+'='+str(dict[i])for i in dict.keys()]
print(c)

lis=[]
for k,v in dict.items():
    print('{}={}'.format(k,v))
    lis.append('{}={}'.format(k,v))
print(lis)
res=' '.join(lis)
print(res)


lis1 = ["AAA","BbB","CCC"]
for i in lis1:
    print(i.lower())

lower=[i.lower() for i in lis1]
print(lower)

i = [(i,j)for i in range(6) for j in range(6) if i%2==0 and j%2==1]

print(i)

# for i in range(100,1000):
#     a=list(str(i)) #元组的元素值不能修改，list()将元组转化为列表
#     #pow(x, y)表示求解x的y次幂
#     #pow(x, y, z)表示求解x的y次幂对z取余后的结果
#     if i == pow(int(a[0]),3)+pow(int(a[1]),3)+pow(int(a[2]),3):
#         print(i)

for i in range(1000,10000):
    a=list(str(i))
    if 10 == int(a[0])+int(a[1])+int(a[2])+int(a[3]):
        print(i)
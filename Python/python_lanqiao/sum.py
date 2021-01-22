n=int(input()) #输入
sum,i,l=0,0,0
a=2 #定值
#假设n=5
#构建5个2,4个20,3个200,2个2000，1个20000相加
for i in range(int(n)):
    l=10**i #python中10**i代表10的i次幂
    sum = sum+(n-i)*a*l
print(sum)

#调用解法
# 载入math库
import math
# math.factorial()函数 作用是返回x的阶乘
print(math.factorial(int(input())))

#for循环解法
n=int(input())
ans=1
for i in range(1,n+1):
    ans*=i
print(ans)

#数组储存方法
n=int(input())
L=[1]#赋初值，不然无法启动
def loop(n):
    global L #Python中定义函数,若想在函数内部对函数外的变量进行操作，就需要在函数内部声明其为global
    for i in range(len(L)):#正常乘法，每位各自乘
        L[i]*=n
    for i in range(len(L)-1):#进位，但是首位进位不在此列
        L[i+1]+=int(L[i]/10)
        L[i]=L[i]%10
    L1=list(str(L[-1]))#分解首项
    L.pop()#删除首项
    for i in range(len(L1)-1,-1,-1):#倒序归入原序列，注意倒叙！！！
        L.append(int(L1[i]))
for i in range(2,n+1):#n！定义
    loop(i)
for i in range(len(L)):#转化形式
    L[i]=str(L[i])
print(''.join(L[::-1]))#join（）输出
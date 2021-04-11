# 2015偶数求和
import sys
n,m=map(int,input().split())
l = []
list_num = 0
num1 = 0  # 计数器
sum = 0
for i in range(n):
    list_num += 2
    l.append(list_num)
for j in range(n):
    sum += l[j]
    num1 += 1
    if num1 == m:
        print(int(sum/m),end=' ')
        num1 = 0  # 计数器清零
        sum = 0  # 和清零
if n%m!=0:
    print(int(sum/(n%m)))
else:
    sys.exit(0)
# 2008数值统计
import sys
num = [float(i) for i in input().split()]
n = num[0]
a,b,c=0,0,0  # 从左到右 负数 0 正数
if n == 0:
    sys.exit(0)
for i in range(1,len(num)):
    if num[i] < 0:
        a += 1
    elif num[i] == 0:
        b += 1
    else:
        c += 1
print(a,b,c)
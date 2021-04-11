# 2012素数判定
import sys
x,y = map(int,input().split())
if x==0 and y==0:
    sys.exit(0)
if x<2: #小于2的数都不算素数
    x=2
if y<2:
    y=2
for i in range(x,y+1):
    ans = i**2+i+41
    for j in range(2,ans):
        if ans%j==0:
            print("Sorry")
            sys.exit(0)
print("OK")

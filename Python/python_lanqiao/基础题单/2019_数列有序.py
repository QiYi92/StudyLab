# 2019数列有序
import sys
n,m = map(int,input().split())
if n==0 and m==0:
    sys.exit(0)

s = [int(i) for i in input().split()]
# 循环s数列，如果s[i]位置的值大于m，则将m插入到s[i]前面
for i in range(n):
    if s[i]>m:
        s.insert(i,m)
        break
for j in range(len(s)):
    print(s[j],end=' ')
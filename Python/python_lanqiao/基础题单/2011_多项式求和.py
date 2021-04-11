# 2011多项式求和
m = int(input())
n = [int(i) for i in input().split()]
sum = 0
float(sum)
for j in range(m):
    for i in range(1,n[j]+1):
        if i % 2 != 0:
            sum += 1/i
        else:
            sum -= 1/i
    print("%.2f"%sum)
    sum = 0

"""
解题思路
本题需要两个循环
因为需要 求m个前n项的和
所以每一个n阶多项式都需要求和
"""


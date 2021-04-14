# 2027n个数的最小公倍数
s = [int(i) for i in input().split()]
n = s[0]
s.remove(s[0])
ans = 0

"""
求多个数的最小公倍数
最大公因数用欧几里得算法（辗转相除法）求出
n个数的思路是求出n1和n1的最大公因数，再把此公因数和n3求最大公因数
最大公因数转换最小公倍数
GCD为最大公因数
再套用公式：最小公倍数=num*num2/GCD
"""
# 两个数求最大公因数（欧几里得算法）
def GCD(num1,num2):
    # 两正整数相除，取被除数和余数成为新的两个数，再相除
    # 当余数为0时，被除数就是最大公因数
    if num2 > num1:
        num1,num2=num2,num1
    while num1 % num2 != 0:
        num1, num2 = num2, num1 % num2
    return num2

# 第一次直接把列表前两个数代入
num1,num2=s[0],s[1]
for i in range(1,n):
    while i!=n:
        num2=s[i]  # 如果列表个数大于2，每次追加一个数
        num1 *= num2 / GCD(num1,num2)  # num1是最小公倍数
        ans = num1
        break
print(int(ans))
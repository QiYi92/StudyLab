# 2006求奇数的乘积
s =[int(i) for i in input().split()]
n = s[0]
ans = 1
for j in range(1,len(s)):
    # 奇数判断
    if s[j] % 2 != 0:
        ans *= s[j]
    else:
        continue
print(ans)
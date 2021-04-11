# 2014评委会打分
s = [float(i) for i in input().split()]
n = s[0]
n_max = 0
n_min = 0
ans = 0
sum = 0
for i in range(1,int(n)):
    if s[i]>n_max:
        n_max = s[i]
    if s[i]<n_min:
        n_min = s[i]
    sum += s[i]
ans = (sum-(n_max+n_min))/(n-2)
print("%.2f"%ans)
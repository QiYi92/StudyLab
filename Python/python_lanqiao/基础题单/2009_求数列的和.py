# 2009求数列的和
import math

# 例子81 4
# 81+√81+√9+√3 --->81+√81+√√81+√√√81
n, m = map(float, input().split())
ans = 0
ans += n
for i in range(1,int(m)):
    ans += math.sqrt(n)
    n = math.sqrt(n)
print("%.2f" % ans)

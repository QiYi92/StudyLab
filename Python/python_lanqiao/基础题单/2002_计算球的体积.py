# 2002计算球的体积
import math
PI=3.1415926
r = float(input())
# 球体体积公式
# 4/3*PI*r^3
ans = 4/3*PI*math.pow(r,3)
print("%.3f"%ans)

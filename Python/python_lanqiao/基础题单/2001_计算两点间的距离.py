# 2001计算两点间的距离
import math
x1,y1,x2,y2 = map(int,input().split())
# 两点间距离公式就是√(x1-x2)^2+(y1-y2)^2
# math.sqrt()是开根函数
# math.pow()是次方函数
# math.pow(x,y)代表x的y次方
ans = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print("%.2f"%ans)

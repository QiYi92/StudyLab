# 2035人见人爱A^B
import sys
while True:
    a,b = map(int,input().split())
    if a == 0 and b ==0:
        sys.exit(0)
    x = a**b
    x = x % 1000
    print(x)
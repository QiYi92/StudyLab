# 2018母牛的故事
# f(n) = f(n-1) + f(n-3)
# 今年的牛 = 去年的牛 + 三年前牛的数量（新出生的牛数量）
import sys
n=int(input())
if n==0:
    sys.exit(0)
f1,f2,f3=1,2,3  # f1第一年的牛,f2第二年的牛,f3第三年的牛
fn=0
if n<=3:
    print(n)
else:
    for i in range(3,n):
        fn = f3 + f1
        f1,f2,f3=f2,f3,fn
    print(fn)
# f(n)=f(n-1)+f(n-3)
# 今年的牛 = 去年的牛 + 三年前牛的数量（新出生的牛数量）
#因为三年前的牛现在每头牛都可以生一头牛

def f(n):
    f1,f2,f3=1,2,3 #f1等于三年前的牛,f2等于两年前的牛,f3等于一年前的牛
    if n<=3: #当值小于等于前三年时直接输出
        return n
    else:
        for i in range(3,n): #从第4年开始计算,当前年份为(i+1)年
            fn = f3 + f1
            f1,f2,f3=f2,f3,fn
    return (fn)
while True:
    n=int(input())
    if n==0: #n=0表示数据结束输出
        break
    print(f(n))


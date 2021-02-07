#封装周期函数
def f(n):
    num=1 #计数器;因为初始值也算一个循环长度，所以从1开始
    while n!=1:
        if n%2==0: #偶数判断
            n=n/2
        else: #奇数
            n=n*3+1
        num+=1 #计数器加一
    return num #返回计数器的值

while True:
    try:
        a,b=map(int,input().strip().split())
        print(a,b,end=" ")
        if a>b: #如果前面的数大则交换
            a,b=b,a
        ma=0
        for i in range(a,b+1): #计数包括a和b，所以循环到b+1
            # 比较大小，把大的赋值给ma
            #直到找出最大的循环长度
            ma=max(ma,f(i))
        print(ma)
    except:
        break
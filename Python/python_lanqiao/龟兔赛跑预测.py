
# v1 v2分别是兔子和乌龟的速度，t是兔子领先阈值，s是兔子休息时间，l是跑道长度
v1,v2,t,s,l=map(int,input().split())
r1=0;t1=0;time=0 # 分别是兔子和乌龟的跑步里程，以及计时器time
while r1<l and t1<l: #当兔子或是乌龟里程等于赛道长度时，结束循环
    r1+=v1 # 兔子
    t1+=v2 # 乌龟
    time+=1 # 计时器+1秒
    if (r1-t1)>=t and r1<l and t1<l:
        for j in range(s): # 兔子休息时间
            t1+=v2 # 乌龟继续走
            time+=1 # 计时器+1
            if r1>=l or t1>=l: # 任意一方走完全程，断开
                break
if r1==t1: #同时到达
    print('D')
elif r1>t1: #兔子到达
    print('R')
else: #乌龟先到达
    print('T')
print(time) #输出时间

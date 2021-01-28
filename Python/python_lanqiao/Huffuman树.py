n=int(input())
pi=list(map(int,input().split())) # 输入n个数
Count=[] # 定义最小费用和的数组，每次找到的pa,pb求和放入Count列表内
ans=0 # 表示最终答案

while len(pi)!=1: #读取pi的长度，当pi长度为1的时候结束
    pi.sort(reverse=True) #将数组从大到小排列
    pa=pi.pop();pb=pi.pop() #将从pi删除的数（最后面）依次赋值给pa,pb
    Count.append(pa+pb)
    pi.append(pa+pb)
for i in range(len(Count)):
    ans+=Count[i] # 将count数组的数依次全部加到ans
print(ans)
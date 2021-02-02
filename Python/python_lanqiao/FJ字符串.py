import copy
N=int(input())
AN=[]
AN.append('A')
for i in range(1,N):
    cp=copy.copy(AN) #将AN列表复制到B列表
    #关键步骤
    # ord('a')是把a转化为对应的ASCII数值，chr('a')是把数字转化为对应的ASCII字符
    AN.append(chr(ord('A')+i)) #将A的下一个字符依次加到AN；第一次+B，第二次+C...
    for k in range(0,len(cp)):
        AN.append(cp[k]) #将B列表的数依次加到AN
for j in range(0,len(AN)): #2**N-1先乘方-1；将AN列表的字符依次输出
    print(AN[j],end='')
print()
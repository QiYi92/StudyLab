count=0 #引入计数器
n=int(input())
al=list(map(int,input().split()))
a=int(input())
for i in range(len(al)):
    if a==al[i]:
        print(i+1) #数列从0开始计算，要知道编号需+1
        count+=1 #如果数列长度为1，则不会触发下面的if
        break
#如果找不到，输出-1
if count==0:
    print(-1)
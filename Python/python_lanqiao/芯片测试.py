n=int(input())
testarray=[] #测试阵列
ans=[] #答案列表
for i in range(n):
    #testarray列表存放芯片的测试结果
    testarray.append(list(map(int,input().split()))) #构造列表
for j in range(n):
    #j循环为被检测的芯片编号循环
    num=0 #被测结果计数器
    for i in range(n): #i循环为检测j芯片的芯片编号循环
        #该行代码的意思是，检测第i个芯片对j个芯片的检测结果是否为1，如果是1则为好芯片
        if testarray[i][j]==1: #检测第i行j列为1
            num+=1 #如果是好芯片，计数器+1
    if num>n/2: #检测计数器的值是否大于芯片总数的1/2，如果true,可知该芯片为好芯片
        print(j+1,end=' ') #输出好芯片的编号
import math  #导入math包
r,c=map(int,input().split())#其中r,c分别代表要输入数据的行数和列数
list1=[]#列表用来存放键盘输入的数据
ans=[]#用来存放要输出的数据
for i in range(0,r):#二维列表输入实例
    list1.append(input().split())
for j in range(0,math.ceil(min(r,c)/2)):#math.ceil（）函数是用来向上取整，向下取整直接整数相除即可，math.ceil(min(r,c)/2表示要转的圈数
    for x in range(j,r-j):#将第j圈的左“1”字形x放入ans；
        ans.append(list1[x][j])
    for y in range(j+1,c-j):#将第j圈的下“一”字形x放入ans;
        ans.append(list1[r-1-j][y])
    if c-1>2*j:#判断一下是否还有多余的列需要转圈
            for p in range(r-j-2,j-1,-1):#将第j圈的右“1”字形放入ans；
                ans.append(list1[p][c-1-j])
    if r-1>2*j:
        for q in range(c-j-2,j,-1):#将第j圈的上“一”字形放入ans；
            ans.append(list1[j][q])
for x in ans:
    print(x,'',end='')

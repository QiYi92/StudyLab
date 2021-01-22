n,m=map(int,input().split()) # 将n和m分别赋值，n为行,m为列
str1=[] # 创建一个空的数据列表
# 从0到m循环，每次对'A'加1个ascii值
for i in range(m):
    # ord()将括号内的字符变为ascii值
    # chr()将括号内的整数变成对应的ascii符号
    # 将对应的字母ascii值+1再变回去
    str1.append(chr(ord('A')+i))
# len()获取列表长度，将表内字母挨个输出
for j in range(len(str1)):
    print(str1[j],end='') #end=''控制不换行
print() #换行
# 使k从1开始循环，这样插入的第一个字母就是B
for k in range(1,n):
    # 用insert()函数从0开始插入一个加过ascii值的字母
    str1.insert(0,chr(ord('A')+k))
    # pop()函数删去表内最后一个字母
    str1.pop()
    # len()获取列表长度，将表内字母挨个输出
    for p in range(len(str1)):
        print(str1[p],end='')
    print()

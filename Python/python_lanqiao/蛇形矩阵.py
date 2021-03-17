#计算每列开头的函数，例如第一列1，第二列2，第三列4,第四列7
def head(n):
    if n <= 1:
        return 1
    return head(n-1)+n-1 #上一行的值+n-1

N = int(input()) #输入一个与矩阵行列数相关的数
alist=[] #定义一个列表
num=0
for j in range(0,N):
    alist1=[] #临时数组
    num=head(j)
    for i in range(j+1,N+1):
        num+=i #计算除了开头外的元素
        alist1.append(num-1) #存到一个列表
    alist.append(alist1) #将临时数组存到此列表
#将数组中的元素依次输出
for i in alist:
    for num in i:
        print(num,"",end="")
    print()

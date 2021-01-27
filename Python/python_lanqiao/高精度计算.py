#python中没有long或者longlong型的数据类型，int类型具有无限精度，所以可以直接求解。
a,b=int(input()),int(input())
print(a+b)

#解法二
def trans(a): # 将输入的字符串变成列表输出
    A=[]
    for i in range(len(a)):
        A.append(eval(a)%10)
        a=a[:-1]
    return A
# eval() 函数用来执行一个字符串表达式，并返回表达式的值
# 例如eval('2 + 2')   >>>4

a=input()
b=input()
A=trans(a)+[0]*(100-len(a))#初始化A，B的长度为100
B=trans(b)+[0]*(100-len(b))
C=[0]*101 #初始化C的长度为101
r=0 #这个是存放的中间变量
for i in range(100):
    o=A[i]+B[i]+r
    C[i]=o%10
    r=o//10
C.reverse()
for i in range(len(C)): #输出结果
    if C[i]!=0:
        for j in C[i:]:
            print(j,end='')
        break
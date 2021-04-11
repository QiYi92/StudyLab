# 水仙花数
m,n = map(int,input().split())
num = 0 #计数器
for i in range(m,n+1):
    b = int(i/100)  #百位
    s = int(i/10)%10  #十位
    g = i%10  #个位
    if i == b**3+s**3+g**3:
        print(i,end=" ")
        num += 1
if num == 0:
    print("no")




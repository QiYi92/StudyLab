
#第一次尝试
n = int(input())
b = []
while n != 1:
    b.append(n)
    a = n
    if a % 2 == 0:
        a = a/2
        n = a
    else:
        a = a * 3 + 1
        n = a
print(int(max(b)))

#第二次尝试
n = int(input())
b = []
c = []
for i in range(1,n+1):
    c.append(i)
for j in c:
    while j != 1:
        b.append(j)
        a = j
        if a % 2 == 0:
            a = a/2
            j = a
        else:
            a = a * 3 + 1
            j = a
print(int(max(b)))


#第三次尝试
n = int(input())
b = []
c = []
for i in range(n,1,-1):
    while i != 1:
        b.append(i)
        a = i
        if a % 2 == 0:
            a = a/2
            i = a
        else:
            a = a * 3 + 1
            i = a
    c.append(max(b))
    b.clear()
print(int(max(c)))



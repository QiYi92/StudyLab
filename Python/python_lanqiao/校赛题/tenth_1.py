n=int(input())
while n!=-1:
    a=input().split()
    for i in range(n):
        if i==0:
            print(a[i],'',end='')
            continue
        if a[i]>a[i-1]:
            print(a[i],'',end='')
    print()
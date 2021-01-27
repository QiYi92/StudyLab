# a=chr(98)
# print(a)

#al=list(map(int,input().split()))

def f(arr):
    for i in range(len(arr)):
        a=chr(arr[i])
        print(a,end='')

al = list(map(int, input().strip().split()))
bl = list(map(int, input().strip().split()))
f(al)
f(bl)
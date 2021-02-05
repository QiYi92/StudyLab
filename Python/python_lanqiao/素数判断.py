# 基础判断方法
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return n != 1
n=int(input())
print(is_prime(n))

#优化算法
import math
def is_prime(n):
    #当n是偶数时不需要循环，因为除了2以外的偶数一定是合数
    if n % 2 == 0 and n != 2:
        return False
    # math,sqrt()返回括号内数的平方根
    #循环到平方根就可以了
    for i in range(3,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return n != 1
n=int(input())
print(is_prime(n))
#
#
#进一步优化算法
def is_prime(n):
    if n % 6 not in (1,5) and n not in (2,3):
        return False
    for i in range(3,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return n != 1

#究极！埃式筛法
def eratosthenes(n): #埃拉托什尼
    primes=[]
    is_prime=[True]*(n+1) #创建一个有n+1个True的列表
    for i in range(2,n+1):
        if is_prime[i]: #将i代入is_prime列表中,如果true则执行，如果false则不执行
            primes.append(i)
            #用当前素数i去筛掉所有能被它整除的数
            for j in range(i*2,n+1,i): #依次取i的倍数; 从i*2开始循环到n+1,步长为i;
                is_prime[j]=False
    return primes
n=int(input())
print(eratosthenes(n))


#蓝桥杯1084题
n=int(input())
primes=[] #素数数列
alist=[True]*(n+1) #整体列表
for i in range(2,n+1):
    if alist[i]: #把i代入整体列表判断,true则继续,false则跳过
        primes.append(i)
        for j in range(i*2,n+1,i):
            alist[j]=False
for i in range(len(primes)):
    print(primes[i])

---
title: 【提高】用筛法求之N内的素数
date: 
author: galileocat
img: https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108051426453.png
top: false
cover: false
coverImg: 
password: 
toc: false
mathjax: false
summary: 蓝桥杯 提高
categories: 蓝桥杯
tags:
  - 蓝桥杯
  - Python
---

题目 1084: 用筛法求之N内的素数。
时间限制: 1Sec 内存限制: 64MB 提交: 14733 解决: 8802
题目描述
用筛法求之N内的素数。
输入
N
输出
0～N的素数
样例输入
100
样例输出
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97

---

**基础判断方法**
素数的性质：只有1和它本身这两个因数
```python
# 基础判断方法
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return n != 1
n=int(input())
print(is_prime(n))

```

**优化算法**
当n是偶数的时候，根本不需要循环，除了2以外的偶数一定是合数。
由此引申出第一种优化方案
```python
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
```
**进一步优化算法**
继续优化，数学上有一个定理，只有形如6n-1和6n+1的自然数可能是素数，这里的n是大于等于1的整数。
因为所有自然数都可以写成6n,6n+1,6n+2,6n+3,6n+4,6n+5这6种，其中6n,6n+2,6n+4是偶数，一定不是素数。6n+3可以写成3(2n+1)，显然也不是素数，所以只有可能6n+1和6n+5可能是素数。6n+5等价于6n-1，所以我们一般写成6n-1和6n+1。
```python
#进一步优化算法
def is_prime(n):
    if n % 6 not in (1,5) and n not in (2,3):
        return False
    for i in range(3,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return n != 1
```
**埃式筛法**
思路就是用已经筛选出来的素数去过滤所有能够被它整除的数。这些素数就像是筛子一样去过滤自然数，最后被筛剩下的数自然就是不能被前面素数整除的数，根据素数的定义，这些剩下的数也是素数。
如果要筛出100以内的所有素数，我们知道2是最小的素数，我们先用2可以筛掉所有的偶数。然后往后遍历到3，3是被2筛剩下的第一个数，也是素数，再用3去筛除所有能被3整除的数。筛完之后我们继续往后遍历，第一个遇到的数是7，所以7也是素数，我们再重复以上的过程，直到遍历结束为止。结束的时候，我们就获得了100以内的所有素数。
**用以下动图辅助理解**
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108070217328.gif)
**算法思路：**
创建两个数组，一个数组放找到的素数(prime)，一个用来判断素数(is_prime)。
用来判断素数的列表用is_prime=[True]*(n+1)生成
生成后的样子[True,True,True,True,True...]
之后从2到n+1开始1循环，将i代入is_prime列表
如果当前i是True，该数为素数
将其放到素数数组内，然后进入2循环
如果当前i是False则直接进入2循环
2循环中依次取i的倍数（不算i），将其变成False
这样每次1循环循环到i的倍数，将不会执行append()
```python
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
```
**蓝桥杯1084题解答
运用到埃式筛法**
```python
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
```
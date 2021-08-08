---
title: 【入门】斐波那契数列
date: 
author: galileocat
img: https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108051426453.png
top: false
cover: false
coverImg: 
password: 
toc: false
mathjax: false
summary: 蓝桥杯 入门训练 Fibonacci数列
categories: 蓝桥杯
tags:
  - 蓝桥杯
  - Python
---

题目 1854: [蓝桥杯][入门训练]Fibonacci数列
时间限制: 1Sec 内存限制: 128MB 提交: 936 解决: 534
题目描述
Fibonacci数列的递推公式为：Fn=Fn-1+Fn-2，其中F1=F2=1。
当n比较大时，Fn也非常大，现在我们想知道，Fn除以10007的余数是多少。
输入
输入包含一个整数n。
输出
输出一行，包含一个整数，表示Fn除以10007的余数。
样例输入
10
样例输出
55
源码

```python
while True:
    try: #try except异常处理机制
        n=int(input()) #输入
        F1,F2=1,1
        #斐波那契数列从3开始到n+1
        for i in range(3,n+1): 
            #F1等于数列里的下一个数，也就是F2
            #F2等于前两项相加
        F1, F2 = F2 % 10007, (F1 + F2) % 10007
    print(F2) #输出在for循环外，不可与for循环同行
    except:
        break
```

### 个人技术博客——二进制的伽利略's Blog
[http://galileocat.cn/](http://galileocat.cn/)
---
title: 【提高】sine之舞
date: 
author: galileocat
img: https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108051426453.png
top: false
cover: false
coverImg: 
password: 
toc: false
mathjax: false
summary: 蓝桥杯 基础练习 sine之舞
categories: 蓝桥杯
tags:
  - 蓝桥杯
  - Python
---
题目 1463: [蓝桥杯][基础练习VIP]Sine之舞
时间限制: 1Sec 内存限制: 128MB 提交: 1912 解决: 1154
题目描述
最近FJ为他的奶牛们开设了数学分析课，FJ知道若要学好这门课，必须有一个好的三角函数基本功。所以他准备和奶牛们做一个“Sine之舞”的游戏，寓教于乐，提高奶牛们的计算能力。
不妨设
An=sin(1–sin(2+sin(3–sin(4+...sin(n))...)
Sn=(...(A1+n)A2+n-1)A3+...+2)An+1
FJ想让奶牛们计算Sn的值，请你帮助FJ打印出Sn的完整表达式，以方便奶牛们做题。
输入
仅有一个数：N<201。
输出
请输出相应的表达式Sn，以一个换行符结束。输出中不得含有多余的空格或换行、回车符。
样例输入
3
样例输出
((sin(1)+3)sin(1-sin(2))+2)sin(1-sin(2+sin(3)))+1

---
解题思路
找到Sn和An的规律
**A1=sin1
A2=sin(1-sin2)
A3=sin(1-sin(2+sin(3)))
A4=sin(1-sin(2+sin(3-sin(4))))**
 
**S1=A1+1
S2=(A1+2)A2+1
S3=((A1+3)A2+2)A3+1
S4=(((A1+4)A2+3)A3+2)A4+1**

**利用递归求解**
```python
def An(n,i=1):
#A1=sin1
#A2=sin(1-sin2)
#A3=sin(1-sin(2+sin(3)))
    if i==n:
        return 'sin('+str(n)+')'
    else:
        if i%2==0: #判断i的奇偶性
            s='+'
        else:
            s='-'
        return 'sin('+str(i)+s+An(n,i+1)+')'
def Sn(m,i=1):
#S1=A1+1
#S2=(A1+2)A2+1
#S3=((A1+3)A2+2)A3+1
    if m==1:
        return An(m)+'+'+str(i) #S1=A1+1
    else:
        return '('+Sn(m-1,i+1)+')'+An(m)+'+'+str(i)
num=int(input())
print(Sn(num)
```


### 个人技术博客——二进制的伽利略's Blog
[http://galileocat.cn/](http://galileocat.cn/)
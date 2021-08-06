---
title: 【提高】回形取数
date: 
author: galileocat
img: https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108051426453.png
top: false
cover: false
coverImg: 
password: 
toc: false
mathjax: false
summary: 蓝桥杯 基础
categories: 蓝桥杯
tags:
  - 蓝桥杯
  - Python
---
题目 1465: [蓝桥杯][基础练习VIP]回形取数
时间限制: 1Sec 内存限制: 128MB 提交: 2313 解决: 754
题目描述
回形取数就是沿矩阵的边取数，若当前方向上无数可取或已经取过，则左转90度。一开始位于矩阵左上角，方向向下。
输入
输入第一行是两个不超过200的正整数m,  n，表示矩阵的行和列。接下来m行每行n个整数，表示这个矩阵。
输出
输出只有一行，共mn个数，为输入矩阵回形取数得到的结果。数之间用一个空格分隔，行末不要有多余的空格。
样例输入
3 3
1 2 3
4 5 6
7 8 9
样例输出
1 4 7 8 9 6 3 2 5
math.ceil(min(r,c)/2)  表示要转的圈数
r=行    c=列
math()函数是用来向上取整
Math.ceil(0.35) ----------> 1
Math.ceil(10) ----------> 10
Math.ceil(-10) ----------> -10
Math.ceil(-10.1)----------> -10
min()函数取当中最小的数,本题中r最小取r,c最小取c
例子
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108070153592.png)
4x4的矩阵
min()取得4，/2，math.ceil()向上取整得2
得出这个回形转2次
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108070154678.png)
5x5的矩阵
min()取得5，/2，math.ceil()向上取整得3
得出这个回形转2次
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108070154166.png)
4x3的矩阵
min()取得3，/2，math.ceil()向上取整得2
得出这个回形转2次
```python
import math #导入math包
r,c=map(int,input().split())#其中r,c分别代表要输入数据的行数和列数
list1=[]#列表用来存放键盘输入的数据
ans=[]#用来存放要输出的数据
for i in range(0,r):#二维列表输入实例
    list1.append(input().split())
for j in range(0,math.ceil(min(r,c)/2)):#math.ceil（）函数是用来向上取整，向下取整直接整数相除即可，math.ceil(min(r,c)/2表示要转的圈数
    for x in range(j,r-j):#将第j圈的左“1”字形x放入ans；
        ans.append(list1[x][j])
    for y in range(j+1,c-j):#将第j圈的下“一”字形x放入ans;
        ans.append(list1[r-1-j][y])
    if c-1>2*j:#判断一下是否还有多余的列需要转圈
        for p in range(r-j-2,j-1,-1):#将第j圈的右“1”字形放入ans；
            ans.append(list1[p][c-1-j])
    if r-1>2*j:
        for q in range(c-j-2,j,-1):#将第j圈的上“一”字形放入ans；
            ans.append(list1[j][q])
for x in ans:
    print(x,'',end='')
```
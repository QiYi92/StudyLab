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
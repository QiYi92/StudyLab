---
title: 【基础】数列排序
date: 
author: galileocat
img: https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108051426453.png
top: false
cover: false
coverImg: 
password: 
toc: false
mathjax: false
summary: 蓝桥杯 基础练习 基础练习
categories: 蓝桥杯
tags:
  - 蓝桥杯
  - Python
---

题目 1853: [蓝桥杯][基础练习]数列排序
时间限制: 1Sec 内存限制: 128MB 提交: 1174 解决: 748
题目描述
给定一个长度为n的数列，将这个数列按从小到大的顺序排列。1<=n<=200
输入
 

第一行为一个整数n。
第二行包含n个整数，为待排序的数，每个整数的绝对值小于10000。
输出
输出一行，按从小到大的顺序输出排序后的数列。
样例输入
5
8 3 6 4 9
样例输出
3 4 6 8 9

---

调用sort()函数方法
```Python
n=int(input())
if n>=1 and n<=200:
    sl=list(map(int,input().split()))
    sl.sort() #sort()排序函数，默认reverse=False从小到大输出,reverse=True则相反
    for i in range(len(sl)):
        print(sl[i],"",end='') #end=' '的作用是输出不换行
```

## 语法
sort()方法语法：
list.sort(cmp=None, key=None, reverse=False)


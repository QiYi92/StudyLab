---
title: 【提高】芯片检测
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

题目 1473: [蓝桥杯][基础练习VIP]芯片测试
时间限制: 1Sec 内存限制: 128MB 提交: 1270 解决: 635
题目描述
有n（2≤n≤20）块芯片，有好有坏，已知好芯片比坏芯片多。
每个芯片都能用来测试其他芯片。用好芯片测试其他芯片时，能正确给出被测试芯片是好还是坏。而用坏芯片测试其他芯片时，会随机给出好或是坏的测试结果（即此结果与被测试芯片实际的好坏无关）。
给出所有芯片的测试结果，问哪些芯片是好芯片。
输入
输入数据第一行为一个整数n，表示芯片个数。
第二行到第n+1行为n*n的一张表，每行n个数据。表中的每个数据为0或1，在这n行中的第i行第j列（1≤i,  j≤n）的数据表示用第i块芯片测试第j块芯片时得到的测试结果，1表示好，0表示坏，i=j时一律为1（并不表示该芯片对本身的测试结果。芯片不能对本  身进行测试）。
输出
按从小到大的顺序输出所有好芯片的编号
样例输入
3
1 0 1
0 1 0
1 0 1
样例输出
1 3

---

**由题意可知
①好芯片比坏芯片多
②用好芯片测试其他芯片，能正确给出被测芯片是好是坏。用坏芯片测试其他芯片会随机给出好坏**
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108070212885.png)
**解题思路为**
所有好芯片对其他好芯片的检测结果都为1，因为坏芯片检测结果不固定，所以我们的判断不能一步到位
首先写一个判断语句，如果检测结果为1，则计数器加1
```python
if testarray[i][j]==1:
    num+=1
```
好芯片比坏芯片数量多，所以用计数器来辅助判断，如果计数器的值大于芯片总数的1/2，说明满足条件
```python
if num>n/2:
```
源码
```python
n=int(input())
testarray=[] #测试阵列
ans=[] #答案列表
for i in range(n):
    #testarray列表存放芯片的测试结果
    testarray.append(list(map(int,input().split()))) #构造列表
for j in range(n):
    #j循环为被检测的芯片编号循环
    num=0 #被测结果计数器
    for i in range(n): #i循环为检测j芯片的芯片编号循环
        #该行代码的意思是，检测第i个芯片对j个芯片的检测结果是否为1，如果是1则为好芯片
        if testarray[i][j]==1: #检测第i行j列为1
            num+=1 #如果是好芯片，计数器+1
    if num>n/2: #检测计数器的值是否大于芯片总数的1/2，如果true,可知该芯片为好芯片
        print(j+1,end=' ') #输出好芯片的编号
```
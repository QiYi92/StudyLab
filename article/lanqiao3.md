---
title: 【基础】杨辉三角
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
题目 1231: 杨辉三角

时间限制: 1Sec 内存限制: 128MB 提交: 2261 解决: 750
题目描述


还记得中学时候学过的杨辉三角吗？具体的定义这里不再描述，你可以参考以下的图形：
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
输入
输入数据包含多个测试实例，每个测试实例的输入只包含一个正整数n（1＜=n＜=30），表示将要输出的杨辉三角的层数。
输出
对应于每一个输入，请输出相应层数的杨辉三角，每一层的整数之间用一个空格隔开，每一个杨辉三角后面加一个空行。
样例输入
2 3
样例输出
1
1 1
1
1 1
1 2 1

```python
al=list(map(int,input().split()))
for a in range(len(al)):
    n=al[a]
    nums=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if j==0:
                nums[i][j]=1
            else:
                nums[i][j]=nums[i-1][j]+nums[i-1][j-1]
            if nums[i][j]!=0:
                print(nums[i][j],"",end='')
        print()
    print()
```
杨辉三角解析
杨辉三角是一道非常经典的题目。我们先来看杨辉三角的一些概述，以下来自百度百科
前提：每行端点与结尾的数为1.
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108070149816.png)
每个数等于它上方两数之和。
每行数字左右对称，由1开始逐渐变大。
第n行的数字有n项。
前n行共[(1+n)n]/2 个数。
第n行的m个数可表示为 C(n-1，m-1)，即为从n-1个不同元素中取m-1个元素的组合数。
第n行的第m个数和第n-m+1个数相等 ，为组合数性质之一。
每个数字等于上一行的左右两个数字之和。可用此性质写出整个杨辉三角。即第n行的第i个数等于第n-1行的第i-1个数和第i个数之和，这也是组合数的性质之一。即 C(n+1,i)=C(n,i)+C(n,i-1)。
通过这些性质我们可以知道一些规律，当然图片会更直观。


### 个人技术博客——二进制的伽利略's Blog
[http://galileocat.cn/](http://galileocat.cn/)
---
title: 【提高】2n皇后问题
date: 
author: galileocat
img: https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108051426453.png
top: false
cover: false
coverImg: 
password: 
toc: false
mathjax: false
summary: 蓝桥杯 提高练习
categories: 蓝桥杯
tags:
  - 蓝桥杯
  - Python
---
题目 1460: [蓝桥杯][基础练习VIP]2n皇后问题
时间限制: 1Sec 内存限制: 128MB 提交: 1353 解决: 684
题目描述
给定一个n*n的棋盘，棋盘中有一些位置不能放皇后。现在要向棋盘中放入n个黑皇后和n个白皇后，使任意的两个黑皇后都不在同一行、同一列或同一条对角线上，任意的两个白皇后都不在同一行、同一列或同一条对角线上。问总共有多少种放法？n小于等于8。
输入
输入的第一行为一个整数n，表示棋盘的大小。
接下来n行，每行n个0或1的整数，如果一个整数为1，表示对应的位置可以放皇后，如果一个整数为0，表示对应的位置不可以放皇后。
输出
输出一个整数，表示总共有多少种放法。
样例输入
4
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
样例输出
2

---

这道题使用两个dfs深度搜索算法来解决，白皇后全部放完后再放入黑皇后。
用两个一维数组存储白皇后和黑皇后的放置位置，数组下标代表行，内容代表列。如ListW[2]代表白皇后在第3行(数组从0开始)的位置
两个函数分别判断白皇后和黑皇后即将放入的位置上面的行中是否有在同一列或者在同一对角线
**具体实行看代码注释**
```python
themax = int(input()) # 获取棋盘边界
canInput = [] # 二维数组来保存能否放置
for i in range(themax):
    canInput.append(list(map(int, input().split())))
ListW = [0] * 8 # 白皇后放置位置
ListB = [0] * 8 # 黑皇后放置位置
nums = 0 # 记录总数
# 检查白皇后是否可以放入
def checkW(row, columu):
    # 如果在第一行则直接放入
    if row == 0:
        return True
    # 循环上面的行中是否存在冲突
    for i in range(row):
        #检测是否有同列;检测是否存在对角线（两边相减的绝对值相等则存在）
        if ListW[i] == columu or abs(row - i) == abs(columu - ListW[i]):
            return False
    return True
# 检查黑皇后是否可以放入
def checkB(row, columu):
    # 如果白皇后在这个位置 则不可放入
    if ListW[row] == columu:
        return False
    # 如果在第一行则直接放入
    if row == 0:
        return True
    # 循环上面的行中是否存在冲突
    for i in range(row):
        if ListB[i] == columu or abs(row - i) == abs(columu - ListB[i]):
            return False
    return True
def dfsW(n):
    # 最后一行被填上时调用黑皇后dfs
    if n == themax: # 如果n等于棋盘边界，则开始放黑皇后dfsB()
        dfsB(0)
    else:
        for i in range(themax):
            if canInput[n][i] == 0: # 判断是否为0，如果为零就跳过此位置
                continue
            elif checkW(n, i) == False: # 调用函数checkW(),如果返回False则继续
                continue
            else:
                # 如果没有出现以上情况
                ListW[n] = i #把值赋值给白皇后数列的第n个数
                dfsW(n + 1) #继续判断下一个数
def dfsB(n):
    # 最后一行被填入时候num+1
    # num+1说明第一种可能性已经跑完
    if n == themax:
        global nums
        nums += 1
    else:
        for i in range(themax):
            if canInput[n][i] == 0:
                continue
            elif checkB(n, i) == False:
                continue
            else:
                ListB[n] = i
                dfsB(n + 1)
dfsW(0)
print(nums)
```


### 个人技术博客——二进制的伽利略's Blog
[http://galileocat.cn/](http://galileocat.cn/)
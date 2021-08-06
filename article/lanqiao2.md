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

## 参数
语法
sort()方法语法：
list.sort(cmp=None, key=None, reverse=False)

## 返回值
cmp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。

**冒泡排序方法**
```Python
def bublle_sort(l):
    #冒泡排序
    n=len(l)
    #一趟只归位出一个数字，如果有n个数字，需要进行n-1趟
    for j in range(n-1):
        count = 0 #计数器归零
        #归位后数字不需要比较，所以每趟只需要比较n-1-j次（j为已执行趟数）
        for i in range(0,n-1-j):
    if l[i] > l[i+1]:
        l[i],l[i+1] = l[i+1],l[i]
        count += 1 #每交换一次，计数器加一
    if 0 == count: #如果计数器为零，也就是无需交换时，结束
        break
if __name__ == "__main__":
    n=int(input())
    alist=list(map(int,input().split()))
    bublle_sort(alist)
    #如果直接print(alist)
    #会输出数组[3,4,5,6,7]
    #题目要求输出3 4 5 6 7
    #故只能用for循环依次输出
    for i in range(len(alist)):
        print(alist[i],"",end='') #" "表示空格,end=' '的作用是输出不换行
```

冒泡排序
第一趟
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108070132164.png)
由于一趟只归为一个数，则如果有n个数字，则需要进行n-1趟。
因为归位后的数字不用再比较了，所以每趟只需要比较n-1-j次（j为已执行的趟数）

len()语法
len()方法语法：
len( s )
参数
s -- 对象。
返回值
返回对象长度。
实例
以下实例展示了 len() 的使用方法：
>>>str = "runoob"
>>> len(str) # 字符串长度
6
>>> l = [1,2,3,4,5]
>>> len(l) # 列表元素个数
5
Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
split()语法
split() 方法语法：
str.split(str="", num=string.count(str)).
参数
str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
num -- 分割次数。默认为 -1, 即分隔所有。
返回值
返回分割后的字符串列表。
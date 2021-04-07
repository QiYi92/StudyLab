# 2000ASCII码排序

"""
join()函数语法
str.join(要连接的元素序列)

例子：
s1 = "-"
s2 = ""
seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
print (s1.join( seq ))
print (s2.join( seq ))


sorted()排序函数
可以从小到大排序 数字，字符，字符串
添加 reverse=True 则改为从大到小
"""

s=input()
print(' '.join((sorted(s))))

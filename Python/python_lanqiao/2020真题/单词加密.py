# 单词加密
n = str(input())
alist = []
for i in range(len(n)):
    num = ord(n[i])
    if num >= 120 or 88 <= num <= 90:
        alist.append(chr(num-23))
    else:
        alist.append(chr(ord(n[i])+3))

for j in range(len(alist)):
    print(alist[j],end='')
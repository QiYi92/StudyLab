# 2025查找最大元素
s = str(input())
str_max = 0
num = 0
sign = []  # 标记点
for i in range(len(s)):
    if ord(s[i]) >= str_max:
        str_max = ord(s[i])
a_num = 0
a_sign = 0
for j in range(len(s)):
    if ord(s[j]) == str_max:
        a_sign += j
        sign.append(a_sign)
        a_num += 1

s_list = list(s)  # 把字符串s变成列表
n = False  # 计数器
if len(sign)>1:
    n = True
for k in range(0,len(sign)):
    if n == False:
        s_list.insert(sign[k], "(max)")
    else:
        s_list.insert(sign[k], "(max)")

s = ''.join(s_list)
print(s)



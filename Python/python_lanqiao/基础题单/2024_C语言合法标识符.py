# 2024C语言合法标识符
# 合法标识符：由字面，数字，下划线组成，开头不能为数字
n = int(input())
for i in range(n):
    s = str(input())
    num = 0  # 计数器
    # 开头判断，开头不能为数字
    if '0' <= s[0] <= '9':
        print('no')
        continue
    for j in range(len(s)):
        # 如果当前字符符合“由字面，数字，下划线组成”，则计数器加一
        if '0' <= s[j] <= '9' or 'a' <= s[j] <= 'z' or s[j]=='_':
            num += 1
            continue
        else:
            print('no')
            break
    if num == len(s):
        print('yes')
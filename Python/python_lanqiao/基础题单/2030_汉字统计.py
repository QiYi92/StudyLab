# 2030汉字统计
n = int(input())
for i in range(n):
    s = str(input())
    num = 0
    for j in range(len(s)):
        # 中文字符范围
        if '\u4e00' <= s[j] <= '\u9fff':
            num += 1
    print(num)
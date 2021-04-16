# 2026首字母变大写
# 首字母变大写函数 str.capitalize()
s = [str(i) for i in input().split()]
for i in range(len(s)):
    ans = s[i].capitalize()
    print(ans,end=' ')
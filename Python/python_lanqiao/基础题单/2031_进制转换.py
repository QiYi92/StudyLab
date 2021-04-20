# 2031进制转换
"""
十进制转R进制规则：
十进制数除以R进制得A，存余数到列表s[]。
再用A除以R进制得A，存余数...直至A=0。
最后所有余数倒置就是转换得数。
"""
n,r = map(int,input().split())
s = []  # 储存余数的数列

# 负数处理
# 负数不能直接转换，要转换为正数然后转换完了再添负号
if n<0:
    print('-',end='')
    n=abs(n)

# 进制转换
# 注意：求出的数倒序输出才是正确值
# 例如：十进制24转2进制，正序输出为00011，倒序输出11000才是正确值
while True:
    s.append(n % r)
    n = int(n / r)
    if n==0:
        break
# 大于10进制转化为字母
for i in range(len(s)):
    if s[i]>10:
        s[i]=chr(ord('A')+s[i]-10)
# 倒序输出
for j in range(len(s)-1,-1,-1):
    print(s[j],end='')
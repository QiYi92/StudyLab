# 2020绝对值排序
import sys
s = [int(i) for i in input().split()]
n = s[0]
if n==0:
    sys.exit(0)
s.remove(s[0])
num = 0

# 冒泡排序
# i表示比较多少轮
for i in range(n-1):
    # j表示每轮比较元素的范围
    # 每过一轮，比较的元素会少i个，所以n-i-1
    for j in range(n-i-1):
        # 如果当前位置的元素小于下一个位置的元素
        if abs(s[j]) < abs(s[j+1]):
            # 则两者交换位置
            s[j],s[j+1]=s[j+1],s[j]

for k in range(n):
    print(s[k],end=' ')




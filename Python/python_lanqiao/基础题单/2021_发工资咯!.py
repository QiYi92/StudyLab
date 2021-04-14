# 2021发工资咯
import sys
n = int(input())
if n==0:
    sys.exit(0)
s = [int(i) for i in input().split()]
money=[100,50,10,5,2,1]
sum = 0  # 人民币张数
# n个老师就有n轮循环
for i in range(n):
    # 每个老师需要的人民币张数
    for j in range(len(money)):
        # 如果s[i]工资比当前币值money[j]少
        # 用int()函数筛除小数点，a取到的值永远是0
        # 例：a = int( 20 / 100 ) = 0
        # 如果如果s[i]工资比当前币值money[j]多
        # a就是所需人民币的张数
        # 例：a = 200 / 100 = 2
        a = int(s[i] / money[j])
        # 把需要的人民币张数加到总和里
        sum += a
        # 利用%取余，把能被当前币值整除的钱数清除
        # 例：s[i] = 250 % 100 ---> s[i] = 50
        s[i] = s[i] % money[j]
print(int(sum))

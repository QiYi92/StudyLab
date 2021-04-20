# 2023求平均成绩
"""
如果n=2 m=2
输入：
5 10 ---> 学生1的2门课成绩
10 20 ---> 学生2的2门课成绩
输出：
7.50 15.00 ---> 2个学生的平均成绩
7.50 15.00 ---> 2门课的平均成绩
"""

n,m = map(int,input().split())  # n学生数,m课程数

alist = []
avg = []
num = 0  # 计数器
ans = 0  # 大于平均成绩同学人数
for i in range(n):
    alist.append([])
    alist[i]=[float(j) for j in input().split()]

# 求n个学生的平均成绩
for j in range(n):
    # 把当前循环的学生的所有课程成绩加起来求平均值
    sum = 0
    for j1 in range(m):
        sum+=alist[j][j1]
    print('%.2f'%(sum/m),end=' ')

print('')

# 求m门课的平均成绩
for k in range(m):
    # 把当前循环的课程的所有学生成绩加起来求平均值
    sum = 0
    for k1 in range(n):
        sum+=alist[k1][k]
    print('%.2f'%(sum/n),end=' ')
    # 创建一个平均值列表
    avg.append(sum/n)

print('')

for p in range(n):
    for q in range(m):
        # 如果大于平均值，计数器加一
        if int(alist[p][q])>int(avg[q]):
            num+=1
    # 如果n同学m科成绩全部达标（计数器num的值等于课程总数）
    # 则达标同学人数加一
    if num==m:
        ans+=1
print(ans)


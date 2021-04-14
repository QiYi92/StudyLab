# 2022海选女主角
m,n = map(int,input().split())
# 创建二维数组
alist = []
for i in range(m):
    alist.append([])
    alist[i]=[int(i) for i in input().split()]

aMax = 0
row = 0  # 横行（m）
column = 0  # 竖列（n）
# 【1】
for j in range(m-1,-1,-1):
    for k in range(n-1,-1,-1):
        if abs(alist[j][k]) >= aMax:
            aMax = abs(alist[j][k])
            row = j
            column = k
# 【2】
print(row+1,column+1,alist[row][column])

"""
【1】
为什么倒着循环？
因为题目设定：
两行同时出现最大分数时，取行号小的
两列同时出现最大分数时，取列号小的
所以倒序输出，当前一个元素值等于上一个元素时
行号，列号大的元素值会被行号，列号小的元素值覆盖
*
例如：一个2x3的数组
2 7 7
7 2 1
输出结果为>>> 1 2 7
*
*
【2】
为什么不能直接输出print( aMax )?
因为aMax储存的是绝对值，如果储存元素本身的值
当负数绝对值大于正数时，aMax里负数会被正数覆盖
"""
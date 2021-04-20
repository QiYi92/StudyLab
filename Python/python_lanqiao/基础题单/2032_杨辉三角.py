# 2032杨辉三角
s = [int(i) for i in input().split()]
for i in range(len(s)):
    n = s[i]
    # 生成一个n阶0矩阵
    nums = [[0]*n for j in range(n)]
    for p in range(n):  # 行
        for q in range(n):  # 列
            if q == 0:
                # 每列第一个数为1
                nums[p][q]=1
            else:
                """每列除了第一个数，所有数的值都等于
                上一行，上一列的数加上上一行，同一列的数
                例子:
                1 2
                1 X 1
                X等于上一行1+2 = 3
                """
                nums[p][q]=nums[p-1][q-1]+nums[p-1][q]
            # 如果当前值不为0，则输出
            if nums[p][q]!=0:
                print(nums[p][q],end=' ')
        print('')
    print('')

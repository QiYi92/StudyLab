n=int(input())
# [[0]*n]*m 直接将[0]*n复制了m遍,m为从1到n
# 假设n=3,就是将[0,0,0]创建了n次
# 此步骤是创建一个二维的n*n零阵
nums=[[0]*n for i in range(n)]
for i in range(n): #竖列
    for j in range(n): #横行
        #每一行第一个数赋值1
        if j==0:
            nums[i][j]=1
        else:
            # 第i行的第j个数等于第i-1行的第j-1个数和第j个数之和
            nums[i][j]=nums[i-1][j-1]+nums[i-1][j]
        if nums[i][j]!=0:
            print(nums[i][j],"",end='') #end=''不换行
    print() #跑完一行后换行


# al=list(map(int,input().split()))
# for a in range(len(al)):
#     n=al[a]
#     nums=[[0]*n for i in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if j==0:
#                 nums[i][j]=1
#             else:
#                 nums[i][j]=nums[i-1][j]+nums[i-1][j-1]
#             if nums[i][j]!=0:
#                 print(nums[i][j],"",end='')
#         print()
#     print()
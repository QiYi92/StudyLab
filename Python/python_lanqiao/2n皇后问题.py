themax = int(input())  # 获取棋盘边界
canInput = []  # 二维数组来保存能否放置
for i in range(themax):
    canInput.append(list(map(int, input().split())))

ListW = [0] * 8  # 白皇后放置位置
ListB = [0] * 8  # 黑皇后放置位置
nums = 0  # 记录总数


# 检查白皇后是否可以放入
def checkW(row, columu):
    # 如果在第一行则直接放入
    if row == 0:
        return True

    # 循环上面的行中是否存在冲突
    for i in range(row):
        #检测是否有同列;检测是否存在对角线（两边相减的绝对值相等则存在）
        if ListW[i] == columu or abs(row - i) == abs(columu - ListW[i]):
            return False
    return True


# 检查黑皇后是否可以放入
def checkB(row, columu):
    # 如果白皇后在这个位置 则不可放入
    if ListW[row] == columu:
        return False

    # 如果在第一行则直接放入
    if row == 0:
        return True

    # 循环上面的行中是否存在冲突
    for i in range(row):
        if ListB[i] == columu or abs(row - i) == abs(columu - ListB[i]):
            return False
    return True


def dfsW(n):
    # 最后一行被填上时调用黑皇后dfs
    if n == themax:  # 如果n等于棋盘边界，则开始放黑皇后dfsB()
        dfsB(0)
    else:
        for i in range(themax):
            if canInput[n][i] == 0:  # 判断是否为0，如果为零就跳过此位置
                continue
            elif checkW(n, i) == False:  # 调用函数checkW(),如果返回False则继续
                continue
            else:
                # 如果没有出现以上情况
                ListW[n] = i #把值赋值给白皇后数列的第n个数
                dfsW(n + 1) #继续判断下一个数

def dfsB(n):
    # 最后一行被填入时候num+1
    # num+1说明第一种可能性已经跑完
    if n == themax:
        global nums
        nums += 1
    else:
        for i in range(themax):
            if canInput[n][i] == 0:
                continue
            elif checkB(n, i) == False:
                continue
            else:
                ListB[n] = i
                dfsB(n + 1)

dfsW(0)
print(nums)
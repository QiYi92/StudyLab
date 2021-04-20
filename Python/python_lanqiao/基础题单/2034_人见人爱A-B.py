# 人见人爱A-B
"""
集合的减法 A-B的意义是:
在集合A中去掉所有与集合B中相同的元素，剩下的内容就是结果。
"""

"""
整体思路：
输入一个数组
先把n和m从数组中提取出来，再把n集合的数和m集合的数分别储存
对n集合数组进行循环
如果n集合中有数在m集合中 [没有出现]
则输出该数，并且计数器+1
如果计数器=0 说明n的数组均在m数组中出现
则输出NULL
"""

import sys
while True:
    s = [int(i) for i in input().split()]
    n, m = s[0], s[1]
    if n == 0 and m == 0:
        sys.exit(0)
    num = 0  # 计数器
    nlist,mlist=[],[]
    s.remove(s[0])
    s.remove(s[0])
    for i in range(n):
        nlist.append(s[i])
    for j in range(n,m+n):
        mlist.append(s[j])
    for q in range(n):
        if mlist.count(nlist[q]) == 0:
            print(nlist[q],end=' ')
            num += 1
    if num == 0:
        print('NULL',end='')
    print('')



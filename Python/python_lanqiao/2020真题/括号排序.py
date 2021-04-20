# # 括号排序
# import itertools
# def check(alist):
#     # 开头不能是反括号
#     if alist[0] == ')':
#         return False
#     stack = []
#     for i in alist:
#         if i == '(':
#             stack.append(i)
#         elif i == ')':
#             if len(stack) == 0 or stack.pop() != '(':
#                 return False
# ans = set()
# alist = list(itertools.permutations(['(',')','(',')','(',')','(',')']))
# for i in alist:
#     if check(i):
#         ans.add(i)
# print(len(ans))


# 括号排序
import itertools


def check(ls):
    if ls[0] == ')':
        return False
    stack = []
    for i in ls:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
    return True

ans = set()
ls = list(itertools.permutations(['(', ')', '(', ')', '(', ')', '(', ')']))
for i in ls:
    if check(i):
        ans.add(i)
print(len(ans))
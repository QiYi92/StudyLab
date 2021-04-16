import itertools
# set()函数 删除重复的字符串
# itertools.permutations()函数 返回每一种可能序列
s=str('LANQIAO')
print(len(set(itertools.permutations(s))))
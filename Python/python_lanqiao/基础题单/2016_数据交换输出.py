# 2016数据交换输出
# 知识点
# list.pop() 删除一个元素
# list.remove() 删除列表一个匹配项
# list.insert() 插入一个元素
# list.index()  找到列表一个匹配项
# list.append()  在列表末尾添加一个新元素
import sys
s = [int(i) for i in input().split()]
n = s[0]
if s[0]==0:
    sys.exit(0)
# list.pop()函数——从列表中移除一个元素
s.pop(0)
num = min(s)  # 导出最小元素
s.remove(min(s))  # 删除最小元素
s.append(num)  # 将导出的最小元素加到最后面
s[-1],s[0]=s[0],s[-1]  # 交换最前面与最后一个数

for i in range(n):
    print(s[i],end=' ')
# 2017字符串统计
# 知识点
# 统计字符串出现的次数
# str.count()
# 统计字符串出现的位置
# str.find()
n = int(input())
for i in range(n):
    sum = 0  # 重置清零
    a = input()
    sum += a.count('1')
    sum += a.count('2')
    sum += a.count('3')
    sum += a.count('4')
    sum += a.count('5')
    sum += a.count('6')
    sum += a.count('7')
    sum += a.count('8')
    sum += a.count('9')
    sum += a.count('0')
    print(sum)
# 2004成绩转换
num = int(input())
# Python中没有 && 和 ||
# 只有 and 和 or
if 100 >= num >= 90:
    print("A")
elif 90 > num >= 80:
    print("B")
elif 80 > num >= 70:
    print("C")
elif 70 > num >= 60:
    print("D")
elif 60 > num >= 0:
    print("E")
else:
    print("Score is error!")

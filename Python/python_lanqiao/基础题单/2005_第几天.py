# 2005第几天

# # 使用datetime库
# import datetime
# num = input()  # 数据格式YYYY/MM/DD
# # 获取num里的数字
# y = int(num[:4])
# m = int(num[5:7])
# d = int(num[8:10])
# # targetday的结果：xxxx-xx-xx
# targetday = datetime.date(y,m,d)
# daycnt = targetday-datetime.date(targetday.year-1,12,31)
# print(daycnt.days)

# 不用库
num = input()
y = int(num[:4])
m = int(num[5:7])
d = int(num[8:10])
sum = 0  # 天数和
# 十二个月的天数
months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
for i in range(m - 1):
    sum += months[i]

sum += d
leap = 0  # 设定leap=1时为闰年
# 闰年判断
if(y%400==0) or (y%4==0 and y%100!=0):
    leap = 1
# 如果当年为闰年 且 月份大于二月
if leap == 1 and m > 2:
    # 天数+1
    sum+=1
print(sum)
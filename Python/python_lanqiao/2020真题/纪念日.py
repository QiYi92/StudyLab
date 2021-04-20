# 纪念日
import datetime

# 年，月，日，小时，分钟，秒
x = datetime.datetime(1921, 7, 23, 12, 0, 0)
y = datetime.datetime(2020, 7, 1, 13, 0, 0)
print(y - x)  # >>> 36138 days,0:00:00
# 天数*小时*分钟
print(36138*24*60)  # >>>52038720

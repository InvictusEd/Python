"""
格式化日历案例
"""

# 时间模块
from datetime import datetime
import calendar

now = datetime.now()
print(now)
print(now.utcnow())
print(now.tzname())
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)
# 格式化输出
# 完整的年
print(now.strftime('%Y'))
# 年后两位数
print(now.strftime('%y'))
# 十进制月份
print(now.strftime('%m'))
# 月份全称
print(now.strftime('%B'))
# 月份简写
print(now.strftime('%b'))
# 星期的十进制
print(now.strftime('%w'))
# 星期简写
print(now.strftime('%a'))
# 星期全称
print(now.strftime('%A'))
print(now.strftime('%Y年%m月%d日 星期%w'))

# print(calendar.prcal(2035, 10))
# for i in range(2):
#     print(i)
#     time.sleep(1)

print(now.today())
print(calendar.month(2022, 12))
print(calendar.weekday(2022, 10, 19))
print(calendar.prcal(2022, m=4))



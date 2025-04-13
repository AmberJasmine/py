from unit import date_unit as date
from unit import com_unit as com

com.headNote("日期计算")
days = date.day_of_year(2025, 4, 14)
print(days)

isleap = date.is_leap_year(2025)
print(isleap)

com.headNote("交换数据")
a=10
b=20
a,b = com.swap(a,b)
print(a,b)
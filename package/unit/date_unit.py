'''工具类
'''


def is_leap_year(year):
    """判断是否为闰年"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def day_of_year(year, month, day):
    """计算给定日期是该年的第几天"""
    # 各月份天数，默认非闰年
    months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        months_days[1] = 29  # 闰年二月29天
    # 计算前几个月的总天数
    total_days = sum(months_days[:month - 1])
    total_days += day
    return total_days

if __name__ == '__main__':
    print(day_of_year(2016, 2, 29))

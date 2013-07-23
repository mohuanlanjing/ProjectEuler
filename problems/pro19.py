#coding: utf-8
"""
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

from calendar import isleap, TextCalendar, Calendar

year = TextCalendar()
first_day = 365%7 + 1
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
count = 0
#print year.pryear(1901)
for i in range(1901,2001):
    if isleap(i):
        days[1] = 29
    else:
        days[1] = 28
    for fd in days:
        first_day = (first_day + fd/7 - 1)%7
        if first_day == 0:
            count += 1
print count


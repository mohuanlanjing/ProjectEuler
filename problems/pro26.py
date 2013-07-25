#coding: utf-8
"""
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

def long_division(num):
    mod_list = []
    quo_list = []
    dividend = 1
    count = 0
    while True:
        while dividend < num :
            mod_list.append(dividend)
            dividend *= 10
            count += 1
        quo_list += (count - 1)*[0]
        mod = dividend % num
        if mod == 0:
            return []
        quo = dividend / num
        dividend = mod
        mod_list.append(mod)
        quo_list.append(quo)
        if mod in mod_list[:-1]:
            return quo_list[mod_list.index(mod):]
        count = 0 

print max([(len(long_division(i)),i) for i in xrange(1,1000)])

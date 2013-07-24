#coding: utf-8
"""
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

def long_division(num):
    borrow = len(str(num))
    import pdb
    pdb.set_trace()
    quo_list = []
    mod_list = []
    mod = 1
    while True:
        temp = mod * pow(10, borrow)
        mod = temp % num
        if mod == 0:
            return []
        quo = temp / num
        if mod_list and quo_list and mod == mod_list[0] and quo == quo_list[0]:
            return quo_list
        quo_list.append(quo)
        mod_list.append(mod)

print long_division(6)
#print max([(long_division(i),i) for i in xrange(1, 1000)])


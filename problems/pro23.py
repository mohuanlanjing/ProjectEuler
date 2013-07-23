#coding: utf-8

"""
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.(below 28123)
"""

from datetime import datetime
from MyAlg import get_list, big_prime

start = datetime.now()
top = 28123 
abundant_list = []
sum_list = []
check_prime = big_prime(limit = top)
for i in xrange(1, top+1):

    if not abundant_list:
        sum_list.append(i)
    else:
        for j in abundant_list:
            if i-j in abundant_list:
                break
            if j == abundant_list[-1]:
                sum_list.append(i)
    if check_prime[i]:
        continue
    if sum(get_list(i)) > i:
        abundant_list.append(i)


for i in xrange(1, top+1):
    if i not in temp_list:
        sum_list.append(i)
print sum(sum_list)
end = datetime.now()
print (end - start).total_seconds()
    

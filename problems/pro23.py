#coding: utf-8

"""
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.(below 28123)
"""

from datetime import datetime
from MyAlg import get_list, big_prime

start = datetime.now()
top = 28123 
abundant_list = []
check_prime = big_prime(limit = top)

# 155 seconds
#sum_list = []
#for i in xrange(1, top+1):

    #if not abundant_list:
        #sum_list.append(i)
    #else:
        #for j in abundant_list:
            #if i-j in abundant_list:
                #break
            #if j == abundant_list[-1]:
                #sum_list.append(i)
    #if check_prime[i]:
        #continue
    #if sum(get_list(i)) > i:
        #abundant_list.append(i)
#print sum(sum_list)

# 10 seconds
bollen_list = [1] * (top + 1)

for i in xrange(1, top+1):
    if check_prime[i]:
        continue
    if sum(get_list(i)) > i:
        abundant_list.append(i)
print abundant_list
size = len(abundant_list)
for i in range(size):
    for j in range(i, size):
        temp = abundant_list[i] + abundant_list[j]
        if temp > top:
            break
        if bollen_list[temp] == 1:
            bollen_list[temp] = 0
s = 0
for i in range(top + 1):
    if bollen_list[i] == 1:
        s += i
print s

end = datetime.now()
print (end - start).total_seconds()
    

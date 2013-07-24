#coding: utf-8
"""
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
# use itertools 55(first time),0.8(after that)          
#from itertools import permutations
#from datetime import datetime

#start = datetime.now()
#print list(permutations(range(10)))[999999]
#end = datetime.now()
#print (end - start).total_seconds()


# use Cantor expansion(immediately)
# http://www.cnblogs.com/1-2-3/archive/2011/04/25/generate-permutation-part2.html
from math import factorial

start = range(10)

def get_mod_list(numth, permutation):
    n = len(permutation)
    mod_list = []
    mod = numth
    for i in xrange(n-1, -1, -1):
        mod_list.append(mod/factorial(i))
        mod = mod%factorial(i)
    return mod_list
        
print [start.pop(i) for i in get_mod_list(999999, start)]



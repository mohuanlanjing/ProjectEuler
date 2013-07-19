#coding: utf-8
"""
What is the value of the first triangle number to have over five hundred divisors?
"""
from datetime import datetime
from MyAlg import primelist,is_prime,big_prime

# get the numst triangle number
def get_triangle(num):
    return sum(range(num+1))

def short_division(num, bp, plist):
    if bp[num]: 
        return [1]
    sdlist = []
    i = 0
    while i < len(plist):
        while num%plist[i] != 0:
            i += 1
        num = num/plist[i]
        sdlist.append(plist[i])
        if bp[num]:
            sdlist.append(num)
            break
        i = 0
    return sdlist

if __name__ == '__main__':
    start = datetime.now()
    i = 2
    tn = 1
    bp = big_prime()
    plist = primelist(1000000)
    while True:
        num = get_triangle(i)
        sdlist = short_division(num, bp, plist)
        l = set(sdlist)
        for j in l:
            tn *= sdlist.count(j)+1
        if tn >= 500:
            print num
            break
        tn = 1
        i += 1
    end = datetime.now()
    print (end-start).total_seconds()
            

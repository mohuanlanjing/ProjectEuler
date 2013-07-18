#coding: utf-8
"""
What is the value of the first triangle number to have over five hundred divisors?
"""
from MyAlg import primelist,is_prime

# get the numst triangle number
def get_triangle(num):
    return sum(range(num+1))

def short_division(num):
    if is_prime(num):
        return [1]
    k = 1
    plist = primelist(k)
    sdlist = []
    i = 0

    while i < len(plist):
        while num%plist[i] != 0:
            if plist[i] == plist[-1]:
                k = k+1
                plist = primelist(k)
            i += 1
        
        if plist[i] == plist[-1]:
            k = k+1
            plist = primelist(k)
        num = num/plist[i]
        sdlist.append(plist[i])
        if is_prime(num):
            sdlist.append(num)
            break
        i = 0
    return sdlist

if __name__ == '__main__':
    i = 2
    tn = 1
    while True:
        num = get_triangle(i)
        sdlist = short_division(num)
        l = set(sdlist)
        for j in l:
            tn *= sdlist.count(j)+1
        print tn
        if tn >= 500:
            print num
            break
        tn = 1
        i += 1

            

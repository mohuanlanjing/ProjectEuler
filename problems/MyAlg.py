from math import sqrt

# check the num is prime number or not
def is_prime(num):
    if not isinstance(num, int):
        raise ValueError,'invaild input'

    if num < 0:
        return False

    if num == 0 or num == 1:
        return False
    
    if num == 2:
        return True

    i = 2
    while i <= int(sqrt(num)):
        if num%i == 0:
            return False
        i += 1
    return True

#make a big prime list below limit
def big_prime(limit=100000000):
    blist = [1] * (limit+1)
    blist[0] = 0
    blist[1] = 0
    max = int(sqrt(limit))
    j = 2
    i = 2
    while i*j<=limit:
        blist[i*j] = 0
        j = j + 1
    j = 2
    for i in range(3,max+1,2):
        if blist[i] == 0:
            continue
        if is_prime(i):
            while i < max and i*j <= limit:
                blist[i*j] = 0
                j += 1
        j = 2
    return blist
    
# return the first num prime list
def primelist(num):
    bp = big_prime(num)
    pl = []
    count = 0
    for i in bp:
        if i:
            pl.append(count)
        count = count + 1
    return pl


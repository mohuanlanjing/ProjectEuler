"""
Collatz Problem
Which starting number, under one million, produces the longest chain?
"""

from datetime import datetime

#return Collatz list starting by num
def collatz(num):
    if not isinstance(num ,int) and num <= 0:
        raise ValueError,"invalid input"

    clist = [num]
    while num != 1:
        if num%2 == 0:
            num = num/2
        else:
            num = 3*num + 1
        clist.append(num)
    return clist
    
if __name__ == '__main__':
    start = datetime.now()
    bigger = 0
    key = 0
    for i in range(1,1000000):
        if len(collatz(i)) > bigger:
            bigger = len(collatz(i))
            key = i
    end = datetime.now()
    print (end-start).total_seconds()
    print key,bigger

"""
Work out the first ten digits of the sum of the following one-hundred 50-digit
numbers 
pro13.txt
"""

f = file('pro13.txt')
addends = [int(i.rstrip()) for i in f.readlines()]
sum = 0
for addend in addends:
    sum += addend
print str(sum)[:10]

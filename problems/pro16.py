#coding: utf-8
"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2**1000?
1<<1000 equals 1*(2**1000)
"""

s = str(1<<1000)
sum = 0
for i in list(s):
    sum += int(i)
print sum

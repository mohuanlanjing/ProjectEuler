#coding: utf-8
"""
Find the sum of the digits in the number 100!
"""
from math import factorial
print sum([int(i) for i in str(factorial(100))])

#coding: utf-8
"""
What is the value of the first triangle number to have over five hundred divisors?
"""
from MyAlg import is_prime

# get the numst triangle number
def get_triangle(num):
    return sum(range(num+1))

if __name__ == '__main__':
    for i in range(30):
        print i,is_prime(i)

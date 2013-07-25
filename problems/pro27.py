#coding: utf-8
"""
Find a quadratic formula that produces the maximum number of primes for consecutive values of n
"""

from MyAlg import primelist, big_prime

check = big_prime(100000)
l = primelist(1000)
l += [-i for i in l]
result = []
for a in l:
    for b in l:
        n = 0
        while True:
            f = n*n + a*n + b
            if not check[f]:
                break
            result.append((n, a, b, a*b))
            n += 1
print max(result)


#coding: utf-8
"""
Evaluate the sum of all the amicable numbers under 10000.
"""

# sum the proper divisor list
def sum_proper_divisors_list(num, option='sum'):
    proper_divisors_list = [i for i in range(1, int(num/2)) if not num%i]
    return sum(proper_divisors_list)

if __name__ == '__main__':
    s = 0 
    for a in range(2,10000):
        da = sum_proper_divisors_list(a)
        if da == 1:
            continue
        db = sum_proper_divisors_list(da)
        if a == db and a != da:
            s += a

print s


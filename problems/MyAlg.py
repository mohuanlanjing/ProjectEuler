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

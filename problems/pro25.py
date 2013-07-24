#coding: utf-8
"""
What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

# return fibonacci list contain num numbers
def fibonacci(num):
    f = [0,1,1]
    for i in xrange(3, num+1):
        f.append(f[-1] + f[-2])
    
    return f 

i = 1
while True:
    if len(str(fibonacci(i)[-1])) == 1000:
        print fibonacci(i).index(fibonacci(i)[-1])
        break
    else:
        i += 1



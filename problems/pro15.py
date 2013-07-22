#coding: utf-8
"""
How many such routes are there through a 20×20 grid?
"""
"""
Because of the move only could be right and down, using 0 stand for move
right and 1 stand for move down.So the problem is becoming a permutation and
combination question with how to fill 40 blank with 20 one and 20 zero.
The answer is C(40,20)
"""
#n = 1 
#num = 2**(n*2)
#count = 0
#for i in range(num):
    #st = bin(i)[2:]
    #if st.count('1') == n:
        #count += 1
#print count

s = 1
d = 1
for i in range(21,41):
    s *= i

for i in range(1,21):
    d *= i

print s/d





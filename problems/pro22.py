#coding: utf-8
"""
What is the total of all the name scores in the file?(pro22.txt)
"""

from string import ascii_uppercase

alp = list(ascii_uppercase)
f = file('pro22.txt')
names = [[j.strip('""') for j in i.split(',')] for i in f.readlines()][0]
f.close()
names.sort()
count = 1
total_score = 0
score = 0
for i in names:
    for j in i:
        if j.isalpha():
            score += alp.index(j) + 1
    total_score += score * count
    score = 0
    count += 1
    k = 0
print total_score


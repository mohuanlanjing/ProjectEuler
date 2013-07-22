#coding: utf-8
"""
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 
"""

#translate number to words
def translate(num):
    dic = { '1' : 'one',
            '2' : 'two',
            '3' : 'three',
            '4' : 'four',
            '5' : 'five',
            '6' : 'six',
            '7' : 'seven',
            '8' : 'eight',
            '9' : 'nine',
            '10': 'ten',
            '11': 'eleven',
            '12': 'twelve',
            '13': 'thirteen',
            '14': 'fourteen',
            '15': 'fifteen',
            '16': 'sixteen',
            '17': 'seventeen',
            '18': 'eighteen',
            '19': 'nineteen',
            '20': 'twenty',
            '30': 'thirty',
            '40': 'forty',
            '50': 'fifty',
            '60': 'sixty',
            '70': 'seventy',
            '80': 'eighty',
            '90': 'ninety'}       
    l = list(str(num))
    word = ''
    max_len = len(l)
    while l:
        count = len(l)
        c = l[0]
        if count == 4 and c != '0':
            word = dic[c] + 'thousand'

        if count == 3 :
            if c == '0' and (l[1] != '0' or l[2] != '0'):
                word += 'and'
            elif l.count('0') == 3:
                pass
            elif l[1] == '0' and l[2] == '0':
                word += dic[c] + 'hundred'
            else:
                word += dic[c] + 'hundred' + 'and'

        if count == 2:
            if c == '0':
                pass
            elif c == '1':
                word += dic[l[0]+l[1]]
                break
            else:
                word += dic[l[0]+'0']
        if count == 1:
            if c == '0':
                pass
            else:
                word += dic[c]
        l.remove(c)
    return word

word = ''
for i in range(1,1001):
    word += translate(i)
print len(word)
        
        

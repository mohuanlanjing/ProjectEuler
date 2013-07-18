#coding: utf-8

f = file('pro11.txt')
data = [i.rstrip().split(' ') for i in f.readlines()]
f.close()
data = [[int(i[j], 10) for j in range(len(i))] for i in data]

product = []
rows = len(data)
cols = len(data[0])

# right scan
for row in data:
    for i in range(cols-3):
        product.append(row[i]*row[i+1]*row[i+2]*row[i+3])

# down scan
for col in range(cols):
    for row in range(rows-3):
        product.append(data[row][col]*data[row+1][col]*data[row+2][col]*data[row+3][col])

# r-d scan
for col in range(cols-3):
    for row in range(rows-3):
        product.append(data[row][col]*data[row+1][col+1]*data[row+2][col+2]*data[row+3][col+3])

# l-d scan
for col in range(cols-4,-1,-1):
    for row in range(rows-3):
        product.append(data[row][col]*data[row+1][col-1]*data[row+2][col-2]*data[row+3][col-3])

print max(product)

        

# Find the second max/min number.

lis = [2, 4, 0, 5, -2, 19, 6]

min = lis[0]
min2 = lis[0]
for n in lis:
    if n < min:
        min2 = min
        min = n

print("Min = ", min) 

print("Min2 = ", min2) 


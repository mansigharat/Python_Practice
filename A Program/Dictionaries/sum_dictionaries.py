#Sum of all values in a dictionary

d1 = {10: 100, 20: 200, 30: 300, 40: 400, 50: 500}

sum =0

for i in d1:
    sum = sum + d1[i]
print("Sum of all values in the dictionary is:", sum)
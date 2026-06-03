l = [12,23,45,67,32,46]

largest = l[0]
sec_largest = l[0]

for i in l:
    if i > largest:
        sec_largest = largest
        largest = i
    elif i > sec_largest:
        sec_largest = i
print(f"Second largest is {sec_largest} and Largest is {largest}")
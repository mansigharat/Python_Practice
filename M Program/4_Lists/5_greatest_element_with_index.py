l = [12,567,43,235,347,568,45,7]

largest = l[0]
index = 0

for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]
        index = i

print(f"Your largest is {largest} at index {index}")
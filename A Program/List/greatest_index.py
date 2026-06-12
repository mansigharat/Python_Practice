l = [14,45,8,2,56,108,7,23,1,67]

largest = l[0]
index = 0

for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]
        index = i

print("Largest element is:", largest)
print("Index of largest element is:", index)
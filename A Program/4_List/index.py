a = [18,19,20,21,22,23,24,25.5]

# for i in range(len(a)):
#     print(a[i])

# for i in a:
#     print(i) 

a.append(26)
print(a)
a.insert(0,17)
print(a)
a.remove(25.5)
print(a)
a.extend([27,28,29,30])
print(a)
popped_item=a.pop(3)
print(a)
index=a.index(21)
print(index)
count_5=a.count(28)
print(count_5)
a.sort()
print(a)
a.reverse()
print(a)
new_a=a.copy()
print(new_a)
a.clear()
print(a)
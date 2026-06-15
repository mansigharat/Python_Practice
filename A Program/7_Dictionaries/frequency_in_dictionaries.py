#Finding frequency of elements in a dictionary

a = [1,1,1,1,2,2,2,3,3,4,4,5,5,4,4,9,6,6,7,7,8,9,8,9,8,9,3,4,4,4]

d = {}

for i in a:
    if i in d:
        d[i] +=1
    else:
        d[i] = 1

print(d)
#Adding common keys in different dictionaries

d1 = {1:10, 2:20, 3:30, 4:40}
d2 = {3:15, 4:25, 5:50, 6:60}

for i in d2:
    if i in d1:
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]
print(d1) 
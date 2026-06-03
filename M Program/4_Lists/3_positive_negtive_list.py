a = [1,3,-9,7,-4,3,6,-5,-10]
pos = []
neg = []
for i in a:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)
print("Positive Numbers : ",pos)
print("Negative Numbers : ",neg)
l= [12,13,14,15,16,17,18]

for i in range(len(l)-1):
    if l[i]<l[i+1]:
        continue
    else:
        print("List is not sorted")
        break
else:
    print("List is sorted")
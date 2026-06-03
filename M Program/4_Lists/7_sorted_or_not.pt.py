a = [1,2,3,4,5,6,7]

for i in range(len(a)-1):
    if a[i] < a[i+1]:
        continue
    else:
        print("Your list is not sorted")
        break
else:
    print("Your list is sorted")
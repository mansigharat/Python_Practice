a = [1,2,3,4,5,6]
for i in range(len(a)):
    if a[i] < a[i+1]:
        continue
    else:
        print("Your list is not sorted")
        break
    
l = [-45,18,45,-7,63,-27,1,-99]

print("Positive Elements are:")
for i in l:
    if i >=0:
        print(i)
print("Negative Elements are:")
for i in l:
    if i < 0:
        print(i)

#yes your code is good , but this can be slow , interviewer may ask second approach too , and also can say it can become more optimize
# as begineer with no prior coding experience (if you wrote without copy paste) this is really good :)
#okay you can optimize this code like this
# let me explain this okay ? suppose 
a = [1,3,-9,7,-4,3,6,-5,-10]  # we have box and that contain flowers and fruits
pos = []   #this bucket for flowers , empty bucket
neg = []    #this bucket for fruits , which is also empty
for i in a:  # we run loop take one by one item from bucket
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)
print("Positive Numbers : ",pos)
print("Negative Numbers : ",neg)
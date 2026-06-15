s = {1, 2, 3, 4, 5}

print(s)

#Adding an element to a set
s.add(6)
print(s)

#Removing an element from a set
s.remove(3)
print(s)    

#Discarding an element from a set
s.discard(4)
print(s)

#popping an element from a set
popped_element = s.pop()
print(f"Popped element: {popped_element}")
print(s)

#Clearing a set
s.clear()
print(s)

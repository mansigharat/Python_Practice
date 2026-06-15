# reading a file
p = open('demo_for_append.txt', 'r') # 'r' is used to read a file

print(p.read())

#creating and appending to a file

r = open('demo_for_append.txt', 'w') # 'w' is used to create a new file, if the file already exists it will overwrite the existing file

r.write('This is a demo file for append') #whatever is written in this parenthesis will be written in the main file

r = open('demo_for_append.txt', 'a') # 'a' is used to append to a file, if the file does not exist it will create a new file
 
r.write('\nI can add as many lines as I want using the append (a)') #whatever is written in this parenthesis will be written in the main file

r.close()

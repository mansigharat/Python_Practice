from pathlib import Path

def readfielandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1}: {items}")


def createfile():
    try:
        readfielandfolder()
        name = input("Enter the name of file you want to create: ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("Enter the data you want to write in file: ")
                fs.write(data)

            print(f"FILE CREATED SUCESSFULLY")
        else:
            print("This file already exists!") 
    except Exception as err:
        print(f"An error occured as {err}")


def readfile():
    readfielandfolder()
    name = input("Which file you wanna read?")
    p = Path(name)
    if p.exists() and p.is_file():
        with open(p,'r') as fs:
            data = fs.read()
            print(data)
        
        print("Readed Sucessfully")

    else:
        print("this")




print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

check = int(input("Enter your choice: "))

if check == 1:
    createfile() 
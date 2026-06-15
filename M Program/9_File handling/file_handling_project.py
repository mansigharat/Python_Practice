from pathlib import Path


def readfileandfolder():
    try:
        path = Path('.')
        items = list(path.glob('*'))

        print("\nFiles and folders:")
        for item in items:
            print(item)

    except Exception as e:
        print("Error:", e)


def createfile():
    try:
        filename = input("Enter file name: ")
        path = Path(filename)

        if path.exists():
            print("File already exists")
        else:
            path.touch()
            print("File created successfully")

    except Exception as e:
        print("Error:", e)


def readfile():
    try:
        filename = input("Enter file name: ")
        path = Path(filename)

        if path.exists():
            data = path.read_text()
            print("\nFile content:")
            print(data)
        else:
            print("File not found")

    except FileNotFoundError:
        print("File does not exist")

    except PermissionError:
        print("Permission denied")

    except Exception as e:
        print("Error:", e)


def updatefile():
    try:
        filename = input("Enter file name: ")
        path = Path(filename)

        if path.exists():
            content = input("Enter content to add: ")
            old_content = path.read_text()

            path.write_text(old_content + "\n" + content)

            print("File updated successfully")

        else:
            print("File not found")

    except PermissionError:
        print("Permission denied")

    except Exception as e:
        print("Error:", e)


def deletefile():
    try:
        filename = input("Enter file name: ")
        path = Path(filename)

        if path.exists():
            path.unlink()
            print("File deleted successfully")

        else:
            print("File not found")

    except PermissionError:
        print("Permission denied")

    except Exception as e:
        print("Error:", e)


try:
    print("""
Press 1 : Creating a file
Press 2 : Reading a file
Press 3 : Updating a file
Press 4 : Deleting a file
Press 5 : Show files/folders
""")

    check = int(input("Enter your choice : "))


    if check == 1:
        createfile()

    elif check == 2:
        readfile()

    elif check == 3:
        updatefile()

    elif check == 4:
        deletefile()

    elif check == 5:
        readfileandfolder()

    else:
        print("Invalid choice")


except ValueError:
    print("Please enter a valid number")

except Exception as e:
    print("Unexpected error:", e)

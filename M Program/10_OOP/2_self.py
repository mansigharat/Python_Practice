class Factory:

    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets
    
    def show(self):
        print(f"Your Object details are {self.material} , {self.pockets} , {self.zips}")

reebook = Factory("leather",2,3)
campus = Factory("Nyolon",4,5)

print(reebook.pockets)
print(campus.material)

reebook.show()
import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists")
    except Exception as err:
        print(f"an exception occured as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(cls.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%^&*?",k=1)
        id = alpha+num+spchar
        random.shuffle(id)
        return "".join(id)
    
    def CreateAccount(self):
        info = {
            "name" : input("Enter your name : "),
            "age" : int(input("Enter your age : ")),
            "email" : input("Enter your Email : "),
            "pin" : int(input("Tell your 4 digit pin : ")),
            "accountNo" : Bank.__accountgenerate(),
            "balance" : 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry You can't create your Account")
        else:
            print("Account has been create successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number")

            Bank.data.append(info)

            Bank.__update()

    def depositmoney(self):
        accnumber = input("Enter Your Account Number : ")
        pin = int(input("Enter your pin : "))
        
        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        if userdata == False:
            print("Sorry no data Found")
        else:
            amount = int(input("How much you want to desposite : "))
            if amount > 10000 or amount < 0:
                print("Sorry the amount is too much , You can deposite below 10000 and above 0")
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited Successfully")

    def withdrawmoney(self):
        accnumber = input("Enter Your Account Number : ")
        pin = int(input("Enter your pin : "))
        
        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        if userdata == False:
            print("Sorry no data Found")
        else:
            amount = int(input("How much money want to withdraw : "))
            if userdata[0]['balance'] < amount:
                print("Sorry You don't have that much money")      
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdrew Successfully")

    def showdetails(self):
        accnumber = input("Enter Your Account Number : ")
        pin = int(input("Enter your pin : "))
        
        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        print("Your Information are \n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")

    def updatedetails(self):
        accnumber = input("Enter Your Account Number : ")
        pin = int(input("Enter your pin : "))
        
        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("No such user Found")
        else:
            print("You can't change your age , account number and balance")
            print("Fill the details for changes or leave it empty if no change")

            newdata = {
                "name" : input("Enter your name : "),
                "email" : input("Enter your Email : "),
                "pin" : input("Tell your 4 digit pin : ")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]["name"]

            if newdata["email"] == "":
                newdata["email"] = userdata[0]["email"]

            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]["pin"]

            newdata["age"] = userdata[0]['age']

            newdata["accountNo"] = userdata[0]['accountNo']

            newdata["balance"] = userdata[0]['balance']

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]
            
            Bank.__update()
            print("Details updated successfully")

    def deletedetails(self):
        accnumber = input("Enter Your Account Number : ")
        pin = int(input("Enter your pin : "))
        
        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("No Data Exists")
        else:
            check == input("Press 'Y' if you actually want to delete else press 'N' if you don't want to delete account")
            if check == 'n' or check == "N":
                print("Bypassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account Deleted Successfully")
                Bank.__update()

user = Bank()

print("Press 1 : Creating Account\nPress 2 : Deposit Money\nPress 3 : Withdrawing Money\nPress 4 : View Details\nPress 5 : Updating the Details \nPress 6 : Delete Account")

check = int(input("Please Enter your choice : "))

if check == 1:
    user.CreateAccount()
elif check == 2:
    user.depositmoney()
elif check == 3:
    user.withdrawmoney()
elif check == 4:
    user.showdetails()
elif check == 5:
    user.updatedetails()
else:
    user.deletedetails()
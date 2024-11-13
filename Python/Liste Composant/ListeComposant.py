#-----------------------------------libraries-----------------------------------
import datetime
#-----------------------------------Function block-----------------------------------
# part= {id, name, type, quantity, price, dateAdded}
partList = []
def showList ():
    for i in partList:
        print(i)
    print("-"*20)

def addPart (part):
    id=part[-1].index + 1
    name= input("Enter the name of the part: ")
    type= input("Enter the type of the part: ")
    while True:
        try:
            quantity= int(input("Enter the quantity of the part: "))
            break
        except:
            print('please enter a valid number')
    while True:
        try:
            price= float(input("Enter the price of the part: "))
            break
        except:
            print('please enter a valid number')
    dateAdded= input("Enter the date of adding the part: (YYYY-MM-DD) ")
    dateAdded = datetime.datetime.strptime(dateAdded, "%Y-%m-%d")
    partList.append({"id":id, "name":name, "type":type, "quantity":quantity, "price":price, "dateAdded":dateAdded})
    print("Part added successfully")

def searchbyid ():
    id= input("Enter the id of the part: ")
    for i in partList:
        if i["id"] == id:
            print(i)
            return
    print("Part not found")

def searchbyname ():
    name= input("Enter the name of the part: ")
    for i in partList:
        if i["name"] == name:
            print(i)
            return
    print("Part not found")

def searchbytype ():
    type= input("Enter the type of the part: ")
    for i in partList:
        if i["type"] == type:
            print(i)
            return
    print("Part not found")

def searchbyDate ():
    dateAdded= input("Enter the date of adding the part: (YYYY-MM-DD) ")
    dateAdded = datetime.datetime.strptime(dateAdded, "%Y-%m-%d")
    for i in partList:
        if i["dateAdded"] == dateAdded:
            print(i)
            return
    print("Part not found")
    
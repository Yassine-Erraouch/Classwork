#A program to manage a crypto currency dictionary


# {"name": "", "symbol": "", "price": , "market_cap": , "volume":     }


#the original dictionary list of crypto currencies
cryptoDict = [
    {"name": "Bitcoin", "symbol": "BTC", "price": 67000.00, "market_cap": 1200000000, "volume": 300000000},
    {"name": "Etherium", "symbol": "ETH", "price": 100.00, "market_cap":  1000000000 , "volume": 125000000},
    {"name": "Dogecoin", "symbol": "DGC", "price": 3.00, "market_cap": 100000000, "volume": 1000},
    {"name": "Zr9alaf", "symbol": "ZR()", "price": 200.00 , "market_cap": 40000000 , "volume": 10000000}
]
#------------------------------------------------------function block -----------------------------------------------
#function to display all cryptos
def display_currencies():
    for item in cryptoDict:
        print(f"{item['name']} | {item['symbol']} | {item['price']} | {item['market_cap']}  | {item['volume']}" )
    return


#function to add a new crypto currency
def add_currency():
    name = input('Enter new Crypto Currency name: ')
    symbol = input('Enter new Crypto symbol: ')
    try:
        price = float(input("enter new crypto currency price: "))
        mrktCap = int(input("Enter new Currency's market cap: "))
        volume = int(input("Eneter new currency's volume: "))
    except:
        print('Invalid value(s)')
    cryptoDict.append({"name": name, "symbol": symbol, "price": price , "market_cap": mrktCap , "volume":volume  })
    print('New Crypto currency Added Successfully.')
    
#function to modify an existing currency's information
def update_currency():
    name= input("Enter the name of the currency you'd like to update: ")
    for item in cryptoDict:
        if name.lower() == item["name"].lower() :
            try:
                newPrice = float(input("Enter new price: "))
                newMrktCap = int(input("Enter new market cap: "))
                newVolume = int(input("Enter new volume"))
            except: 
                print("invalid value(s)")
            item["price"] = newPrice
            item["market_cap"] = newMrktCap
            item["volume"] = newVolume
            print("Information updated successfuly.")
            return
    else:
        print("This currency does not exist.")

#function to delete currency
def remove_currency():
    name = input("Enter the name of the currency you'd like to remove: ")
    for item in cryptoDict:
        if name.lower() == item["name"].lower():
            cryptoDict.pop(item)
            print("Currency removed successfuly.")
            return
    print("This currency does not exist.")
    
#fucntion to find a currency
def find_currency():
    name = input("Enter the name of the currency you'd like to find: ")
    for item in cryptoDict:
        if name.lower() == item["name"].lower():
            print(f"{item['name']} | {item['symbol']} | {item['price']} | {item['market_cap']}  | {item['volume']}" )
        else:
            return
    print('This currency does not exist.')        

#function to filter dictionary list by price  
# def higher_or_lower_than():
#     try:
#         compPrice= int(input('Enter your comparaison price'))
#     except:
#         print("Invalid value.")
#         compChoice = input(f'Would you like to see currencies with a lower price than {compPrice} or higher | (1:higher, 2:lower)')
#         if compChoice == '1':
#             higherList = filter(lambda x: x> compPrice, item['price'] for item in cryptoDict)
#             lowerList = 
            
#-----------------------------------------------menu----------------------------------------
while True:
    print('-'*20)
    print("1.Display all currencies")
    print("2.Add a new currency")
    print("3.Update a currency's information")
    print("4.Remove a currency")
    print("5.Find a currency by name")
    print("0.Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        display_currencies()
    elif choice == "2":
        add_currency()
    elif choice == "3":
        update_currency()
    elif choice == "4":
        remove_currency()
    elif choice == "5":
        find_currency()
    elif choice == "0":
        break
    else:
        print('Invalid choice, Choose again.')
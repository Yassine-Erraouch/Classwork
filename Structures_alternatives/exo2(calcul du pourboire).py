#ask user for their bill amount
while True:
    try:
        billAmount = float(input("Enter the amount of the bill: "))
        break
    except:
        print('please enter a valid number')

#ask a user for the quality of service they recieved [excellent, good, bad]
while True:
        qualityOfService = input("Choose the quality of service | 1 for excellent, 2 for good, 3 for bad: ")
        if qualityOfService == '1':
            total = billAmount * 1.2
            print("Your total is:", total)
            break
        elif qualityOfService == '2':
            total = billAmount * 1.15
            print("Your total is:", total)
            break
        elif qualityOfService == '3':
            total = billAmount * 1.05
            print("Your total is:", total)
            break
        else: 
            print('please enter a valid value')

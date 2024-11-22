from datetime import datetime, timedelta, time




#-----------------------------------------------------------Functions-----------------------------------------------------------



#a function that takes a date then adds a number of days and gives back the date
def add_date():
    while True:
        try:
            date, days = input('Enter a date in the format of dd/mm/yyyy: '), int(input('Enter number of days to add: '))
            date_obj = datetime.strptime(date, "%d/%m/%Y")
            break
        except:
            print('invalid value(s). Please try again.')
    
    new_date = date_obj + timedelta(days=days)
    return new_date

#a function that takes a date then subtracts a number of days and gives back the date

def sub_date():
    while True:
        try:
            date, days = input('Enter a date in the format of dd/mm/yyyy: '), int(input('Enter number of days to subtract: '))
            date_obj = datetime.strptime(date, "%d/%m/%Y")
            break
        except:
            print('invalid value(s). Please try again.')
    
    new_date = date_obj - timedelta(days=days)
    return new_date

#a function that takes a number of milliseconds then returns how many hours, minutes and seconds it is equivalent to

def msConvert():
    while True:
        try:
            ms = int(input('Enter number of milliseconds: '))
            break
        except:
            print('invalid value. Please try again.')
    days = ms // (24 * 60 * 60 * 1000)
    hours = (ms % (24 * 60 * 60 * 1000)) // (60 * 60 * 1000)
    minutes = (ms % (60 * 60 * 1000)) // (60 * 1000)
    seconds = (ms % (60 * 1000)) // 1000
    time_object = f'{days} days, {hours} hours, {minutes} minutes and {seconds} seconds'
    return time_object

#--------------------------------------------------Menu----------------------------------------------

while True:
    print('1. Add days')
    print('2. Subtract days')
    print('3. Convert milliseconds to hours, minutes and seconds')
    print('4. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        print(add_date())
    elif choice == '2':
        print(sub_date())
    elif choice == '3':
        print(msConvert())
    elif choice == '4':
        break
    else:
        print('Invalid choice. Please try again.')
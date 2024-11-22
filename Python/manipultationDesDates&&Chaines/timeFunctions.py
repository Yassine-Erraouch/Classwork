from datetime import datetime, timedelta, time




#-----------------------------------------------------------Functions-----------------------------------------------------------



#a function that takes a date then adds a number of days and gives back the date
# def add_date():
#     while True:
#         try:
#             date, days = input('Enter a date in the format of dd/mm/yyyy: '), int(input('Enter number of days to add: '))
#             date_obj = datetime.strptime(date, "%d/%m/%Y")
#             break
#         except:
#             print('invalid value(s). Please try again.')
    
#     new_date = date_obj + timedelta(days=days)
#     return new_date

def add_date(date, criteria):
    years = criteria["years"]
    months = criteria["months"]
    days = criteria["days"]
    hours = criteria["hours"]
    minutes = criteria["minutes"]
    seconds = criteria["seconds"]
    milliseconds = criteria["milliseconds"]
    new_date = date + timedelta(years=years, months=months, days=days, hours=hours, minutes=minutes, seconds=seconds, milliseconds=milliseconds)
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
    
    new_date = abs(date_obj - timedelta(days=days))
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

#function that calculates the difference between two dates

def diff_date():
    while True:
        try:
            date1, date2 = input('Enter first date in the format of dd/mm/yyyy: '), input('Enter second date in the format of dd/mm/yyyy: ')
            date1, date2 = datetime.strptime(date1, "%d/%m/%Y"), datetime.strptime(date2, "%d/%m/%Y")
            break
        except:
            print('invalid value(s). Please try again.')
    return abs(date2 - date1)


#---------------------------------------------------function parameters ---------------------------------------------------


#--------------------------------------------------Menu----------------------------------------------

while True:
    print('1. Add days')
    print('2. Subtract days')
    print('3. Convert milliseconds to hours, minutes and seconds')
    print('4. Calculate difference between two dates')
    print('5. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        criteria = {"years": 0, "months": 0, "days": 0, "hours": 0, "minutes": 0, "seconds": 0, "milliseconds": 0}
        date = datetime.strptime(input('Enter a date in the format of dd/mm/yyyy: '), "%d/%m/%Y")
        try:
            criteria["years"] = int(input('Enter number of years: '))
            criteria["months"] = int(input('Enter number of months: '))
            criteria["days"] = int(input('Enter number of days: '))
            criteria["hours"] = int(input('Enter number of hours: '))
            criteria["minutes"] = int(input('Enter number of minutes: '))
            criteria["seconds"] = int(input('Enter number of seconds: '))
            criteria["milliseconds"] = int(input('Enter number of milliseconds: '))
        except:
            print('invalid value(s). Please try again.')

        time_object = date + timedelta(**criteria)
        print(time_object)
        print(add_date())
    
    elif choice == '2':
        print(sub_date())
    elif choice == '3':
        print(msConvert())
    elif choice == '4':
        print(diff_date())
    elif choice == '5':
        break
    else:
        print('Invalid choice. Please try again.')
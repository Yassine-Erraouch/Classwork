import datetime

# ask user to enter date
userDate = input("Enter a date in the format YYYY-MM-DD: ")
#check if the input is valid

#get the year, month and date from the input
year = int(userDate[0:4])
month = int(userDate[5:7])
date = int(userDate[8:10])
#calculate the day of the week
day = datetime.date(year, month, date).weekday()
if day in [0,1,2,3,4]:
    print("the day is a weekday")
else:
    print("the day is a weekend day")

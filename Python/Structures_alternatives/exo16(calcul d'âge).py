import datetime
#ask user to enter date of birth in this format dd/mm/yyyy
while True:
    try:
        dateOfBirth = input("Enter your date of birth in the format dd/mm/yyyy: ")
        dateOfBirth = datetime.datetime.strptime(dateOfBirth, "%d/%m/%Y")
        break
    except:
        print('please enter a valid date')
#if date is in the future print error else calculate age
if dateOfBirth > datetime.datetime.now():
    print("Error:Please enter a valid date of birth")
else: 
    age = datetime.datetime.now() - dateOfBirth
    age = age.days // 365
    print("You are", age, "years old")

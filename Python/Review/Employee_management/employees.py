import re
from datetime import *

# creating patterns
firstname_pattern = r"[A-Za-z]{2,}(\s[A-Za-z]{2,})*"
surname_pattern = r"[A-Za-z]{2,}(\s[A-Za-z]{2,})*"
date_pattern = r"\d{2,}-\d{2}-\d{4}"





# creating custom error
class InvalidStartDateError(Exception):
    def __init(self, message):
        self.message = message

class InvalidFirstNameError(Exception):
    def __init(self):
        self.message = "Invalid first name"

class InvalidSurnameError(Exception):
    def __init(self):    
        self.message = "Invalid surname"

class InvalidDateOfBirthError(Exception):
    def __init(self, message):
        self.message = message

class Employee:
    def __init__(self, id, firstname, surname, date_of_birth, start_date, salary):
        self.id = id
        self.firstname = firstname
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.start_date = start_date
        self.salary = salary
        # checking if the attributes match the set patterns
        if not re.match(firstname_pattern, self.firstname):
            raise InvalidFirstNameError
        if not re.match(surname_pattern, self.surname):
            raise InvalidSurnameError
        if not re.match(date_pattern, self.date_of_birth):
            raise InvalidDateOfBirthError("Date of birth must be in the format dd-mm-yyyy")
        if not re.match(date_pattern, self.start_date):
            raise InvalidStartDateError("Start date must be in the format dd-mm-yyyy")
        
        sdate = datetime.strptime(self.start_date, "%d-%m-%Y")
        bdate = datetime.strptime(self.date_of_birth, "%d-%m-%Y")
        
        # checking if the dates are correct
        if not sdate:
            raise InvalidDateOfBirthError("Date of birth is invalid")
        if not bdate:
            raise InvalidStartDateError("Start date is invalid")
        
    
        if sdate < bdate + timedelta(days=24*365):
            raise InvalidStartDateError("Start date must be at least 24 years after date of birth")


    def __str__(self):
        return f"First name: {self.firstname} | Last name: {self.surname} | Date of birth: {self.date_of_birth} | Start date: {self.start_date} | Salary: {self.salary}"
    
    def __eq__(self, other):
        return self.id == other.id
    
    
    def calculate_seniority(self):
        sdate = datetime.strptime(self.start_date, "%d-%m-%Y")
        current_date = datetime.now()
        seniority = (current_date - sdate).days // 365
        return f"{self.firstname} {self.surname} worked in the company for {seniority} years"
    
    def calculate_age(self):
        bdate = datetime.strptime(self.date_of_birth, "%d-%m-%Y")
        current_date = datetime.now()
        age = (current_date - bdate).days // 365
        return age
    
    def calculate_retirement_date(self):
        time_till_retirement = 65 - self.calculate_age()
        current_date = datetime.now()
        retirement_date = current_date + timedelta(days=time_till_retirement * 365)
        return f"{self.firstname} {self.surname} will retire in {time_till_retirement} years" 
    
    
employee_1 = Employee(1, "John", "Doe", "10-01-1980", "15-05-2005", 50000)
employee_2 = Employee(2, "Jane", "Smith", "23-11-1975", "01-02-2000", 60000)
employee_3 = Employee(3, "Alice", "Johnson", "30-03-1990", "18-07-2015", 55000)
employee_4 = Employee(4, "Bob", "Brown", "12-06-1985", "11-09-2010", 52000)
employee_5 = Employee(5, "Charlie", "Davis", "05-09-1978", "22-03-2003", 58000)

employee_7 = Employee(7, "Frank", "Green", "21-08-1983", "30-06-2008", 57000)
employee_8 = Employee(8, "Grace", "Black", "09-04-1981", "25-05-2006", 59000)
employee_9 = Employee(9, "Henry", "Gray", "14-07-1986", "05-11-2011", 56000)
employee_10 = Employee(10, "Isabel", "Blue", "03-05-1979", "19-08-2004", 61000)


employee_1.calculate_age()
employee_1.calculate_seniority()
employee_1.calculate_retirement_date()

print(employee_1)
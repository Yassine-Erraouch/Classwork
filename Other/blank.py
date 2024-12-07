try: 
    choice = int(input("Enter a number: "))
except:
    print('invalid value')
    
    
def use_choice (choice):
    choice += 10
    return choice

print(use_choice(choice))
from datetime import datetime

def is_date_palindrome (date):
    date = date.replace("-", "")
    date = list(date)
    revDate = date.reverse()
    return date == revDate


while True:
    try:
        date = input("Entrez une date au format jj-mm-aaaa: ")
        if datetime.strptime(date, "%d-%m-%Y"):
            break
    except:
        print("La date n'est pas au bon format. Veuillez réessayer.")

if is_date_palindrome(date):
    print("La date est un palindrome.")
else:
    print("La date n'est pas un palindrome.")


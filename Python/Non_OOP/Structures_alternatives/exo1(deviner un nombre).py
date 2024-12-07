import random

secretNumber = random.randint(1,100)

attempts = 0
# asking the user for their guess
while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < secretNumber:
            print("Too low!")
            attempts += 1
        elif guess > secretNumber:
            print("Too high!")
            attempts += 1
        else:
            print("You got it!, the secret number was", secretNumber, "it took you", attempts, "attempts to guess")
            break
    except:
        print('please enter a valid integer')
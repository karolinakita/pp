import random

number=random.randint(1,3)
guess = int(input("Guess a number (1,2,3): "))

if guess == number:
    print("Congrats! You guessed the number!")
else:
    print("Sorry, myślałem o liczbe " + str(number))

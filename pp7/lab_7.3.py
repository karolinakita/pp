import random

number=random.randint(1,10)
guess = int(input("Guess a number (1-10): "))

if guess == number:
    print("Congrats! You guessed the number!")
elif guess > number:
    print("Niestety nie,ale masz jeszcze dwie próby! Liczba jest mniejsza..")
elif guess < number:
    print("Niestety nie, ale masz jeszcze dwie próby! Liczba jest większa..")

guess = int(input("Guess a number (1-10): "))
if guess == number:
    print("Congrats! You guessed the number!")
elif guess > number:
    print("Niestety nie,ale masz jeszcze jedną próbę! Liczba jest mniejsza..")
elif guess < number:
    print("Niestety nie, ale masz jeszcze jedną próbę! Liczba jest większa..")

guess = int(input("Guess a number (1-10): "))
if guess == number:
    print("Congrats! You guessed the number!")
elif guess > number:
    print("Niestety nie, liczba o której myślałem to", number)
elif guess < number:
    print("Niestety nie, liczba o której myślałem to", number)
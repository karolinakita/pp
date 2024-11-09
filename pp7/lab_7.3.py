# import random
#
# number=random.randint(1,10)
# guess = int(input("Guess a number (1-10): "))
#
# if guess == number:
#     print("Congrats! You guessed the number!")
# elif guess > number:
#     print("Niestety nie,ale masz jeszcze dwie próby! Liczba jest mniejsza..")
# elif guess < number:
#     print("Niestety nie, ale masz jeszcze dwie próby! Liczba jest większa..")
#
# guess = int(input("Guess a number (1-10): "))
# if guess == number:
#     print("Congrats! You guessed the number!")
# elif guess > number:
#     print("Niestety nie,ale masz jeszcze jedną próbę! Liczba jest mniejsza..")
# elif guess < number:
#     print("Niestety nie, ale masz jeszcze jedną próbę! Liczba jest większa..")
#
# guess = int(input("Guess a number (1-10): "))
# if guess == number:
#     print("Congrats! You guessed the number!")
# elif guess > number:
#     print("Niestety nie, liczba o której myślałem to", number)
# elif guess < number:
#     print("Niestety nie, liczba o której myślałem to", number)
#

import random

number1=random.randint(1,10)
msg="Guess a number (1-10): "
guess1=int(input(msg))

if guess1==number1:
    print("Brawo! Zgadłeś!")
else:
    msg = "Masz kolejną szansę, moja liczba jest "
    if number1 % 2 == 0:
        msg += "parzysta "
    else:
        msg+= "nieparzysta "
    guess1=int(input(msg))
    if guess1==number1:
        print("Brawo udało się zgadnąć za drugim razem!")
    else:
        msg="Masz ostatnią szansę. Moja liczba jest "
        if number1 > 5:
            msg += "większa niż"
        else:
            msg+= "mniejsza lub równa "
        msg+="pięć "
        guess1 = int(input(msg))
        if guess1 == number1:
            print("Brawo udało się zgadnąć za trzecim razem!")
        else:
            print("Niestety moja liczba to " + str(number1))
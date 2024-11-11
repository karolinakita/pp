import random

number=random.randint(1,10)
msg="Zgadnij liczbę z przedziału 1 do 10: "
guess = int(input(msg))

if guess == number:
    print("Udało się, zgadłeś liczbę!")
else:
    msg="Niestety, nie udało ci się. Ale masz jeszcze dwie próby. Liczba o której myślę jest "
    if number %2==0:
        msg += "parzysta: "
    else:
        msg += "nieparzysta: "
    guess = int(input(msg))
    if guess == number:
        print("Udało się, zgadłeś liczbę!")
    else:
        msg = "Niestety, nie udało ci się. Ale masz jeszcze jedną próbę. Liczba o której myślę jest "
        if number > 5:
            msg += "większa od 5: "
        else:
            msg += "mnijesza od 5: "
        guess = int(input(msg))
        if guess == number:
            print("Udało się, zgadłeś liczbę!")
        else:
            print("Niestety, nie udało ci się. Miałem na myśli liczbę " + str(number))
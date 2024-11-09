# gra toczy się dopóki nie zostanie odgadnięta liczba
import random
counter=1
number = random.randint(1, 10)
guess = int(input("Zgadnij jaką liczbę mam na myśli od 1 do 10: "))

while guess != number:
    guess = int(input("nie, to nie ta. spróbuj jeszcze raz: "))
    counter += + 1
print("Brawo, udało ci się za " + str(counter))
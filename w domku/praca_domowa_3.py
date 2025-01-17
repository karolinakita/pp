import random


liczba_graczy =int(input("Podaj liczbę graczy: "))
imiona = []
counter = 1
poprzednie_slowo=None
ostatni_gracz = None
for i in range(liczba_graczy):
    imię = input("Podaj imię gracza: ")
    imiona.append(imię)
    counter += 1
print(imiona)
while True:
    while True:
        losowe_imie = random.choice(imiona)
        if losowe_imie != ostatni_gracz:
            break
        print("Gra: ",losowe_imie)
    if poprzednie_slowo == None:
        poprzednie_slowo = str(input(f"{losowe_imie}, podaj pierwsze słowo: "))
        continue
    losowe_imie = random.choice(imiona)
    print(f"Gra: {losowe_imie}")
    sprawdzenie = input("Podaj poprzedni wyraz: ")
    if sprawdzenie == poprzednie_slowo:
        poprzednie_slowo=input("Gratuluję. Podaj kolejne słowo: ")
    else:
        print("Koniec gry")
        print("\n"*5)
        break
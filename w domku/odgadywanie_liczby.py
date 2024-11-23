tajna_liczba = 9
zgadnij = None

while zgadnij != tajna_liczba:
    zgadnij=int(input("Podaj liczbę: "))
    if zgadnij > tajna_liczba:
        print("Za dużo")
    elif zgadnij < tajna_liczba:
        print("Za mało")
print("Brawo")
# skrypt pobiera liczbę od użytkownika
# wyświetla info czy dana licza jest parzysta i czy jest podzielna przez 5 i 7

number= int(input("Enter a number: "))
print("liczba jest")

if number % 2 == 0:
    print("Licza jest parzysta")
else:
    print("Licza jest nieparzysta")

if number % 5 == 0:
    print("Licza jest podzielna przez 5")
else:
    print("Licza jest niepodzielna przez 5")

if number % 7 == 0:
    print("Licza jest podzielna przez 7")
else:
    print("Licza jest niepodzielna przez 7")
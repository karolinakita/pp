numbers_total = int(input("Podaj liczbę elemntów zbioru: "))

def no_duplicates():
    numbers = []
    counter = 1
    while counter <= numbers_total:
        number = int(input("Podaj element zbioru: "))
        if number not in numbers:
            numbers.append(number)
        counter +=1

    print(numbers)

no_duplicates()
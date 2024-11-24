import random

numbers = []
count = 0
for i in range(16):
    number = random.randint(1, 6)
    numbers.append(number)
    if number == 6:
        count += 1
print("Oto zestaw wylosowanych oczek kostki", numbers)
print("Oto liczaba wylosowana za 8 razem: ", numbers[7])
print("Liczba wyrzuconych szóstek: ", count)
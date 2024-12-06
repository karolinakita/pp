import random

zbior = []
wielkosc_zbioru = 6
for i in range(wielkosc_zbioru):
    zbior.append(random.randint(0,6))
print(zbior)

frequency =[0,0,0,0,0,0,0]
for i in zbior:
    frequency[i] += 1

print(frequency)
most_common = 0
for i in range(wielkosc_zbioru):
    if frequency[i]>frequency[most_common]:
        most_common = i

print("Najczęściej występującą cyfrą jest", most_common)

range_from = int(input("Zakres od: "))
range_to = int(input("Zakres do: "))

print("Liczby z zakresu od " + str(range_from) + " do " + str(range_to) + " są podzielne przez 3 lub 5 lub 7")
for i in range(range_from,range_to +1):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        print(i)
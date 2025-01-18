# numbers = []
# counter = 1
#
# while True:
#     if counter > 5:
#         break
#     try:
#         number = int(input("Podaj liczbę całkowtitą "))
#         numbers.append(number)
#         counter += 1
#     except:
#         print("To nie jest liczba całkowta")
#
# print(numbers)

# liczba = int(input("Podaj liczbę wierszy i kolumn:"))
# for i in range (liczba):
#     print(i)
macierz = []
for i in range(1,11):
    wiersz = [i] * 10
    macierz.append(wiersz)

for wiersz in macierz:
    print(wiersz)

# row_1 = [1]*liczba
# row_2 = [2]*liczba
# row_3 = [3]*liczba
# matrix = [row_1,row_2,row_3]
# print(matrix)
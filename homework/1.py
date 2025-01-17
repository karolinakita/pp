# liczby = int(input("Podaj ilość liczb: "))
suma_parzystych = 0
suma_nieparzystych = 0
# a =int(0)
# for i in range(a):
#     a = int(input("Podaj liczbę: "))
#     if a % 2 ==0:
#         suma_parzystych += a
#     else:
#         suma_nieparzystych += a
#
# print(suma_parzystych)
# print(suma_nieparzystych)

while True:
    liczba = input("podaj liczbę: ")
    if liczba == "":
        break
    liczba_1 = int(liczba)
    if liczba_1 % 2 == 0:
        suma_parzystych += liczba_1
    elif liczba_1 % 2 != 0:
        suma_nieparzystych += liczba_1

print('Suma liczb parzystych: ', suma_parzystych)
print('Suma liczb nieparzystych: ', suma_nieparzystych)
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

enter = str("")
liczba = int(input("podaj liczbę: "))
while liczba:
    liczba = int(input("podaj kolejną liczbę: "))
    if liczba % 2 == 0:
        suma_parzystych += liczba
    elif liczba % 2 != 0:
        suma_nieparzystych += liczba
    elif int(""):
        break



print(suma_parzystych)
print(suma_nieparzystych)
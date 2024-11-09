# a=input("Podaj znak: ")
# b=input("Podaj liczbę kolumn: ")
# c=input("Podaj liczbę wierszy: ")
#
# print((a*int(b)+"\n")*int(c))

a=int(input("Podaj rozmiar: "))
b=input("Podaj znak: ")

for i in range(a):
    for j in range(a):
        print(b,end=" ")
    print()
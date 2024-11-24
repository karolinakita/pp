liczba_imion = int(input("Ile imion chcesz podać? "))
lista_imion=[]
for i in range(liczba_imion):
    imię = input("Podaj imię: ")
    lista_imion.append(imię)
print(lista_imion)
zarobki = float(input("Podaj swoje zarobki (zł): "))

if zarobki < 3000:
    print("Podatek wynosi", zarobki*0.1, "zł. Po odliczeniu podatku zostaje", zarobki - (zarobki*0.1))
elif zarobki <7000:
    print("Podatek wynosi", zarobki * 0.15, "zł. Po odliczeniu podatku zostaje", zarobki - (zarobki * 0.15))
elif zarobki >= 7000:
    print("Podatek wynosi", zarobki * 0.2, "zł. Po odliczeniu podatku zostaje", zarobki - (zarobki * 0.2))
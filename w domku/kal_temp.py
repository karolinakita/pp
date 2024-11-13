wybor = int(input("Wybierz konwersję: (1) Celsjusz na Fahrenheit, (2) Fahrenheit na Celsjusz: "))
temp = int(input("Podaj temperaturę: "))

if wybor == 1:
    print(temp, "C to ", float((temp * 9/5)) + 32, "F")
elif wybor == 2:
    print(temp, "F to ", round(float((temp - 32) * 5/9),2), "C")
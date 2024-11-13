number = int(input("Wprowadź liczbę: "))
x = int(input("Podaj numer bitu: "))


# maska
mask = 1 << x
result = number & mask
bit = int(bool(result))

print("Bit na pozycji", x, "dla liczby", number, "wynosi", str(bit))
print()
# sprawdzenie
print("{:08b}".format(number))
print("{:08b}".format(mask))
print("-"*8)
print("{:08b}".format(result))
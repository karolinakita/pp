phones={
    "Ania": 123456789,
    "Basia": 321654987,
    "Adam": 789456123,
    "Bolek": 456785236
}
# print(phones)
def get_number():
    while True:
        ask = input("Enter name: ")
        if ask =="":
            break
        if ask in phones.keys():
            print("Numer telefonu: ", phones[ask])
        else:
            print("Nie znaleziono telefonu dla imienia", ask, "w słowniku")


get_number()
import random
first_symbol = "A"
last_symbol = "H"
number_of_letters = 6
def wylosuj_litere():
    return chr(random.randint(ord(first_symbol), ord(last_symbol)))

def wylosuj_wiersz():
    return [wylosuj_litere() for _ in range(number_of_letters)]

def sprawdzenie(wiersz):
    first_element = wiersz[0]
    for element in wiersz:
        if first_element != element:
            return False
        else:
            return True


counter = 1
while True:
    wiersz = wylosuj_wiersz()
    print(wiersz, counter)
    if sprawdzenie(wiersz):
        break
    counter += 1
# print(sprawdzenie(wylosuj_wiersz()))

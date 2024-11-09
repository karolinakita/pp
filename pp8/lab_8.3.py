sum = 0
for i in range(64):
    sum += 2 ** i

print("Suma wszystkich ziaren na szachownicy: " + str(sum))

#założenia: waga 1 ziarna to 0,4mg -> 0,0004g
#1kg = 1000g
#1t = 1000kg

tons = int(sum*0.0004/1000/1000)
print(tons, 'ton')

#roczna produkcja pszenicy na świecie to 782 mln ton
years = int(tons/782000000)
print("Starczy na " + str(years) + ' lat')

#pociąg może przetransportować 2200t
trains = int(tons/2200)
print(trains, 'pociągów')
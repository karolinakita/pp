import random

komp = random.choice(["papier", "kamień", "nożyce"])
print(komp)
wybór = input("Wybierz papier, kamień lub nożyce ")

# if komp == wybór:
#     print("Remis")
# elif komp == "papier" and wybór == "kamień":
#     print("Papier pokonuje kamień. Przegrana")
# elif komp == "kamień" and wybór == "papier":
#     print("Papier pokonuje kamień. Wygrana")
# elif komp == "kamień" and wybór == "nożyce":
#     print("Kamień pokonuje nożyce. Przegrana")
# elif komp == "nożyce" and wybór == "kamień":
#     print("Kamień pokonuje nożyce. Wygrana")
# elif komp == "nożyce" and wybór == "papier":
#     print("Nożyce pokonują papier. Przegrana")
# elif komp == "papier" and wybór == "nożyce":
#     print("Nożyce pokonują papier. Wygrana")
#
if komp == wybór:
    print("Remis")
elif (komp == "kamień" and wybór == "papier") or (komp == "nożyce" and wybór == "kamień") or (komp == "papier" and wybór == "nożyce"):
    print("Wygrana")
else:
    print("Przegrana")
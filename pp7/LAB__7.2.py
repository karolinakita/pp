points=int(input("Wprowadż liczbę punktów uzyskanych przez ucznia (1-100): "))

if points >= 95:
    print("Ocena 5.0")
elif points > 84:
    print("Ocena 4.5")
elif points >= 70:
    print("Ocena 4.0")
elif points > 60:
    print("Ocena 3.5")
elif points >= 50:
    print("Ocena 3.0")
else:
    print("Ocena 2.0")
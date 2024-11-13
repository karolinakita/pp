poprawna_nazwa="kaka129"
poprawne_haslo="haslo"

nazwa=input("Wprowadź nazwę użytkownika: ")
hasło=input("Wprowadź hasło: ")

if nazwa == poprawna_nazwa and hasło ==poprawne_haslo:
   print("Zalogowano pomyślnie!")
else:
   print("Nieprawidłowa nazwa użytkownika lub hasło")
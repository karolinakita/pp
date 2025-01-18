from lotto import get_user_numbers, draw_numbers, check_numbers

print("Witaj w grze")
user_numbers = get_user_numbers()
print("Pobrane liczby to: ", user_numbers)

print("\nNaciśnij enter aby dokonać losowania liczb\n")
input()
lucky_numbers = draw_numbers()
print("wyosowano liczby:", lucky_numbers)
print()

result = check_numbers(user_numbers,lucky_numbers)
if result ==6:
    print("Gratulacje")
elif result ==5:
    print("Brawo, tafiłeś piątkę")
elif result ==4:
    print("Czwórka")
elif result ==3:
    print("Trójka")
elif result ==2 or result ==1:
    print("trafiono {} liczby/ę".format(result))
else:
    print("nic")
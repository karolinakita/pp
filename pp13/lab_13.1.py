# import random
# def potega(a):
#     return a ** a
#
#
# liczby = []
# ilość_liczb = int(input("Podaj ilość liczb: "))
# # random.randint(1, 100))
# for i in range(ilość_liczb):
#     liczby.append(random.randint(1, 10))
# print(liczby)
# # print(liczby[2])
# # print(potega(liczby[0]))
#
# for i in range(ilość_liczb):
#     print(potega(liczby[i]))


def pow(numbers, exponent):
    numbers = numbers[:]
    for i in range(len(numbers)):
        numbers[i] = numbers[i]**exponent
    return numbers

numbers = [1,2,3,4,5]
print(pow(numbers, 2))

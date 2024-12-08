# numbers = 1,2,3,4,5
# numbers = (1,2,3,4,5)
# # print(numbers)
# #
# # numbers = ()
# # print(numbers)
#
# # for number in numbers:
# #     print(number)
#
# print(numbers[:])
#
# numbers=tuple(x for x in range(10) if x%2==0)
# print(numbers)

# numbers = (1,2,3)
# numbers[0]=999
# del numbers[0]
# del numbers
# print(len(numbers))
# print(numbers*2)
# print(numbers+numbers)
#
# numbers= [1,2,3]
# print(numbers)
# numbers = tuple(numbers)
# print(numbers)

# letters = tuple("ala ma kota")
# print(letters)

# słowniki
# phones = {"Tomek": 123456789, "Tomi": 987654321, "Chujek": 123789456}
# print(phones)

# animals_dictionary = {
#     "kot": "cat",
#     "pies": "dog",
#     "chomik": "hamster"
}
# print(animals_dictionary)
#
# print(animals_dictionary["kot"])
# print(animals_dictionary.get("wiewiórka", "Brak klucza w słowniku"))

# words = ["kot", "lew","chomik"]
# for word in words:
#     if word in animals_dictionary.keys():
#         print(word, '->', animals_dictionary[word])
#     else:
# #         print("Nie znaleziono słowa", word, "w słowniku")
#
# for key in animals_dictionary:
#     print(key, '->', animals_dictionary[key])
#
# print()
#
# for value in animals_dictionary.values():
#     print(value)
#
# print()
#
# for item in animals_dictionary.items():
#     print(item)
#
# for key, value in animals_dictionary.items():
#     print(key, value)

# animals_dictionary['świnka'] = 'pig'
# print(animals_dictionary)
# animals_dictionary.popitem()
# print(animals_dictionary)
#
# animals_dictionary.clear()
# print(animals_dictionary)
# i= 0
# #dopóki
# while i < 10:
#     print(i, end=" ")
#     i +=1
#
# for i in range(10):
#     print(i, end=" ")
# #początek 3, koniec <10, skaczemy co 2
# for i in range(3, 10, 2):
#     print(i, end=" ")
#
# for i in range(9, -1, -1):
#     print(i, end=" ")

#silnia 3! = 1*2*3 = 6

number = 5
factorial = 1
# for i in range(1, number+1):
#     factorial *= i
# print(factorial)

#
# while number:
#     factorial *= number
#     number -= 1
# print(factorial)

for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("koniec pętli")
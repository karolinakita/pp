# # # temp = 12
# # # is_sun_shining= False
# # #
# # # if temp > 0 and is_sun_shining :
# # #     print("spacer")
# # # else:
# # #     print("not spacer")
# # #
# # # # jeżeli będzie ujemna tem lub bedzie pochmurnie to zostajemy w domu jezeli nie to idziemy na spacer
# # # if not(temp < 0 or not is_sun_shining) :
# # #     print("spacer")
# # # else:
# # #     print("not spacer")
# #
# # #operatory logiczne
# # # and = czytamy jak i
# # #or = czytamy jak lub
# # # not = jak nie
# #
# # # iterujeny od 0-9 (10 iteracji)
# # # wyświetlamy cyfrę chyba że..
# # #liczba parzysta lub większa od 6 to wyświetl *
# # #
# # # for i in range(10):
# # #     if i % 2 == 0 or i > 6:
# # #         print("*")
# # #     else:
# # #         print(i)
# #
# # # pobieramy od uzytkownika dlugosci 3 odcikow
# # # sprawdz czy mozna z nich zbudowac trojkat
# # # sprawdz jaki to bedzie trojkat ze wzgledu na boki (roznoboczny, rownoboczny, rownoramienny)
# # # ze wzgledu ma katy(prostokatny, ostrokatny, rozwartokatny)
# # print("Podaj dlugosci 3 odcinków, (liczby calkowite)")
# # a=int(input("a: "))
# # b=int(input("b: "))
# # c=int(input("c: "))
# #
# # if a+b >c and a+c >b and b+c >a:
# #     print("Mozna zbudowac trojkat", end=" ")
# #     if a==b and a==c and b==c:
# #         print("równoboczny", end=" ")
# #     elif a==b or a==c or b==c:
# #         print("równoramienny", end=" ")
# #     else:
# #         print("różnoramienny", end=" ")
# #     if  a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or c ** 2 + a ** 2 == b ** 2:
# #         print("prostokątny", end=" ")
# #     elif a ** 2 + b ** 2 < c ** 2 or b ** 2 + c ** 2 < a ** 2 or c ** 2 + a ** 2 < b ** 2:
# #         print("rozwatrokątny")
# #     else:
# #         print("ostrokątny")
# # else:
# #     print("Nie mozna")
#
# a, b, c= 2, 3, 4
# if a<b and b<c:
#     print("!!!")
#
# a= 5
# b = 3
#
# # koniunkcja bitowa
# print(a, "&", b, "=", a & b)
# print("{:08b}".format(a))
# print("{:08b}".format(b))
# print("-"*8)
# print("{:08b}".format(a&b))
# # alternatywa bitowa
# print(a, "|", b, "=", a | b)
# print("{:08b}".format(a))
# print("{:08b}".format(b))
# print("-"*8)
# print("{:08b}".format(a|b))
#
# # alternatywa rozłączna bitowa
# print(a, "^", b, "=", a ^ b)
# print("{:08b}".format(a))
# print("{:08b}".format(b))
# print("-"*8)
# print("{:08b}".format(a^b))
#
# # przesunięcie bitowe w prawo
# print(a, ">>", b, "=", a >> b)
# print("{:08b}".format(a))
# print("-"*8)
# print("{:08b}".format(a>>b))
#
# # przesunięcie bitowe w lewo
# print(a, "<<", b, "=", a << b)
# print("{:08b}".format(a))
# print("-"*8)
# print("{:08b}".format(a<<b))
#
# # negacja bitowa
# print("~"+ str(a), "=", ~a)
# print("{:08b}".format(a))
# print("-"*8)
# print("{:08b}".format(~a))

print(~1)
K
#00000001 (1)
# 00000000 (0)
# 11111111 (-1)
# 11111110 (-2)

for i in range(5, -6,-1):
    print("{0:08b} => {1:d}".format(*args: i & 255, i))
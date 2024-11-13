ocena_1=int(input("Podaj mi pierwszą ocenę (punkty 1-100): "))
ocena_2=int(input("Podaj mi drugą ocenę (punkty 1-100): "))
ocena_3=int(input("Podaj mi trzecią ocenę (punkty 1-100): "))

średnia=(ocena_1+ocena_2+ocena_3)/3
if średnia== 100:
    print("Gratulacje! Otrzymałeś najlepszą ocenę!")
elif średnia >=90:
    print("Ocena końcowa: 5")
elif średnia >= 80:
    print("Ocena końcowa: 4")
elif średnia >= 70:
    print("Ocena końcowa: 3")
elif średnia >= 60:
    print("Ocena końcowa: 2")
else:
    print("Ocena końcowa: 1")

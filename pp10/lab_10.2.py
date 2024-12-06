import random

numbers = []
count = 0
for i in range(16):
    number = random.randint(1, 6)
    numbers.append(number)
    if number == 6:
        count += 1


print("Oto zestaw wylosowanych oczek kostki", numbers)
print("Oto liczaba wylosowana za 8 razem: ", numbers[7])
print("Liczba wyrzuconych szóstek: ", count)


in_row_value_tmp=numbers[0]
in_row_total_tmp=0
in_row_value=0
in_row_total=0

for i in range(16):
    if i == in_row_value_tmp:
        in_row_total_tmp+= 1
    else:
        in_row_value_tmp=i
        in_row_total_tmp = 1
    if in_row_total_tmp > in_row_total:
        in_row_value = in_row_value_tmp
        in_row_total = in_row_total_tmp
print("Pod rząd wyrzucono", in_row_total, "razy wartość", str(in_row_value))
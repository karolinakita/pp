# 1, 2 , 4, 8 ,16,....
# 0, 1, 2, 3, 4, 5,
sum=0
for i in range (64):
   sum += 2 ** i
print(sum)
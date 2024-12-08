# numbers_1= [1,2,3]
# numbers_2= [1,2,6,7]
# numbers_3= [6,7,8]
# numbers = tuple(numbers_1 + numbers_2 + numbers_3)
# print(numbers)
#
# for number in numbers:
#     if number != numbers[number-1]:
#         print(number)
#     # print(numbers[0])
#     # if numbers[number]

def merge_list_wihout_dulicates(source, target):
    for element in source:
        if element not in target:
            target.append(element)

def transform_data(list1,list2,list3):
    resoult = []
    merge_list_wihout_dulicates(list1,resoult)
    merge_list_wihout_dulicates(list2, resoult)
    merge_list_wihout_dulicates(list3, resoult)
    return tuple(resoult)

print(transform_data([1,2],[1,1],[4,4,4]))
print(transform_data([1,2,3],[1,2,3],[4,5,6]))
print(transform_data(["Ala","ma","kota"],["Ala","ma"],["Ala","ma","mysz"]))
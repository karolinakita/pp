"""This is my first own module"""


def is_string(val):
    """Simple string validator"""
    return isinstance(val, str)


def sum_list_elem(list):
    sum = 0
    for i in list:
        sum += i
    return sum


if __name__ == '__main__':
    print(is_string("abc") == True)
    print(is_string(123) == False)
    print(sum_list_elem([1, 1, 1]) == 3)
    print(sum_list_elem([]) == 0)

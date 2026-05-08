import re


def multiply_numbers(user_string: str = None):
    if user_string == None:
        return None

    if type(user_string) != str:
        user_string = str(user_string)

    my_number_list = []
    result = 1

    for char in user_string:
        if re.search(r"[0-9]", char):
            my_number_list.append(int(char))

    if not my_number_list:
        return None

    for number in my_number_list:
        result *= number

    return result


def tests():
    print(multiply_numbers()) # => None
    print(multiply_numbers('ss')) # => None
    print(multiply_numbers('1234')) # => 24
    print(multiply_numbers('sssdd34')) # => 12
    print(multiply_numbers(2.3)) # => 6
    print(multiply_numbers([5, 6, 4])) # => 120


tests()

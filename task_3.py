def max_odd(arr: list):
    my_list = []
    for i in arr:
        if isinstance(i, (int, float)) and i % 2 != 0:
            my_list.append(round(i))

    if my_list == []:
        return None

    max_element_from_list = max(my_list)

    return max_element_from_list


def tests():
    print(max_odd([1, 2, 3, 4, 4]))  # => 3
    print(max_odd([21.0, 2, 3, 4, 4]))  # => 21
    print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))  # => 3
    print(max_odd(['ololo', 'fufufu']))  # => None
    print(max_odd([2, 2, 4]))  # => None


tests()

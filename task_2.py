def coincidence(user_list = None, user_range = None):
    if user_list is None or user_range is None:
        return []

    edited_list = []
    for i in user_list:
        if type(i) == float or int and i in user_range:
            edited_list.append(i)

    return edited_list


def tests():
    print(coincidence([1, 2, 3, 4, 5], range(3, 6)))  # => [3, 4, 5]
    print(coincidence())  # => []
    print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))  # => [1, 2, 2.5]


tests()

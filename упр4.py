def sort_list(user_list: list = []):
    if user_list == []:
        return []

    min_element_from_user_list = min(user_list)
    max_element_from_user_list = max(user_list)

    for i in range(len(user_list)):
        if user_list[i] == max_element_from_user_list:
            user_list[i] = min_element_from_user_list
        elif user_list[i] == min_element_from_user_list:
            user_list[i] = max_element_from_user_list

    user_list.append(min_element_from_user_list)

    return user_list


def tests():
    print(sort_list([])) # => []
    print(sort_list([2, 4, 6, 8])) # => [8, 4, 6, 2, 2]
    print(sort_list([1])) # => [1, 1]
    print(sort_list([1, 2, 1, 3])) # => [3, 2, 3, 1, 1]


tests()

def connect_dicts(user_dict_1: dict[str, int], user_dict_2: dict[str, int]):
    copy_user_dict_1 = {}
    for key, value in user_dict_1.items():
        if value >= 10:
            copy_user_dict_1[key] = value

    copy_user_dict_2 = {}
    for key, value in user_dict_2.items():
        if value >= 10:
            copy_user_dict_2[key] = value

    sum_1 = sum_dict(copy_user_dict_1)
    sum_2 = sum_dict(copy_user_dict_2)

    if sum_1 >= sum_2:
        result_dict = copy_user_dict_1
        result_dict.update(copy_user_dict_2)
    else:
        result_dict = copy_user_dict_2
        result_dict.update(copy_user_dict_1)

    result_dict = sorted(result_dict.items(), key=lambda x: x[1])

    return dict(result_dict)

def sum_dict(user_dict: dict[str, int]) -> int:
    result = sum(user_dict.values())
    return result


def tests():
    print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))
    # =>{'c': 11, 'b': 12}
    print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))
    # =>{'d': 11, 'c': 12, 'a': 13}
    print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))
    # =>{'c': 11, 'b': 12, 'a': 15}

tests()

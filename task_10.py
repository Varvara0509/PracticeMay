import re


def count_words(string: str) -> dict:
    if string != type(str):
        string = str(string)

    my_dict = {}
    string = re.sub(r"[^a-zA-Z0-9]", " ", string)
    string = string.lower()
    split_string = string.split()

    for word in split_string:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1

    return my_dict


def tests():
    print(count_words("A man, a plan, a canal -- Panama")) # => {'a': 3, 'man': 1, 'plan': 1, 'canal': 1, 'panama': 1}
    print(count_words("Doo bee doo bee doo")) # => {'doo': 3, 'bee': 2}


tests()

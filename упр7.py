def combine_anagrams(arr: list[str]) -> list[list[str]]:
    new_arr = []
    for word in arr:
        new_arr.append(word.lower())

    d = {}
    for word in new_arr:
        d.setdefault(tuple(sorted(word)), []).append(word)
    return list(d.values())


def tests():
    print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]))
    # => [['cars', 'racs', 'scar'], ['for'], ['potatoes'], ['four'], ['creams', 'scream']]

tests()

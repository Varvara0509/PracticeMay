import re


def is_palindrome(usual_string = None) -> bool:
    if usual_string == None:
        return False

    if type(usual_string) != str:
        usual_string = str(usual_string)

    clean_string = re.sub(r"[^a-zA-Z0-9]", '',  usual_string)
    clean_string = clean_string.lower()
    return clean_string == clean_string[::-1]


def tests():
    print(is_palindrome("A man, a plan, a canal -- Panama")) # => True
    print(is_palindrome("Madam, I'm Adam!")) # => True
    print(is_palindrome(333)) # => True
    print(is_palindrome(None))# => False
    print(is_palindrome("Abracadabra"))# => False


tests()

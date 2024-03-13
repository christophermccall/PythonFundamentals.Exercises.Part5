def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    new_val = value.lower().replace(" ","")
    return new_val[0:] == new_val[::-1]  # remove pass statement and implement me

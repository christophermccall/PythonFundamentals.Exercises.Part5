def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    compare1 = sorted(first_string)
    compare2 = sorted(second_string)  # remove pass statement and implement me

    return compare2 == compare1

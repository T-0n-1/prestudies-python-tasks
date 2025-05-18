def times_ten(start: int, end: int) -> dict:
    """
    This function takes a dictionary as input and returns a new dictionary
    where each value is multiplied by 10.
    
    :param start: The starting value of the dictionary keys.
    :param end: The ending value of the dictionary keys.
    :return: dict
    """
    dictionary = {}
    for key in range(start, end + 1):
        dictionary[key] = key * 10
    return dictionary


d  = times_ten(3, 6)
print(d)

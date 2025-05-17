def double_items_in_list(input_list: list) -> list:
    """
    This function takes a list of integers and returns a new list with each integer doubled.

    :param input_list: List of integers
    :return: New list with each integer doubled
    """
    return [item * 2 for item in input_list]


luvut = [2, 4, 5, 3, 11, -4]
tuplaluvut = double_items_in_list(luvut)
print("alkuperäinen:", luvut)
print("tuplattu:", tuplaluvut)
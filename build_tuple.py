def build_tuple(x: int, y: int, z: int) -> tuple:
    """
    Build a tuple from three integers.
    First element is the biggest of then, second is the smallest, and the third is the sum of arguments.

    Args:
        x (int): The first integer.
        y (int): The second integer.
        z (int): The third integer.

    Returns:
        tuple: A tuple containing the three integers.
    """
    temp_list = []
    temp_list.append(x)
    temp_list.append(y) 
    temp_list.append(z)
    highest = max(temp_list)
    lowest = min(temp_list)
    sum_of_params= sum(temp_list)
    return (highest, lowest, sum_of_params)


print(build_tuple(5, 3, -1))
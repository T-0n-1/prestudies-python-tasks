def swap_keys_with_values(dictionary: dict) -> dict:
    """
    Swap keys with values in a dictionary.
    
    Args:
        dictionary (dict): A dictionary with keys and values to swap.
        
    Returns:
        dict: A new dictionary with keys and values swapped.
    """
    return {value: key for key, value in dictionary.items()}


s = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas"}
vaihdettu = swap_keys_with_values(s)
print(vaihdettu)
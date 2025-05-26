def change_size(string: str) -> str:
    """
    Change the size of the character in string by replacing lower ones with upper and vice versa.
    
    : Param string: The input string to change the size of characters.
    : Return: The modified string with character sizes changed.
    """
    reversed_string = ""
    for char in string:
        if char.islower():
            reversed_string += char.upper()
        elif char.isupper():
            reversed_string += char.lower()
        else:
            reversed_string += char
    return reversed_string


def split_the_string(string: str) -> tuple:
    """
    Split the string into two parts: the first half and the second half.
    
    : Param string: The input string to split.
    : Return: A tuple containing the first half and the second half of the string.
    """
    mid_index = len(string) // 2
    return string[:mid_index], string[mid_index:]


def remove_special_characters(string: str) -> str:
    """
    Remove special characters from the string.
    
    : Param string: The input string from which to remove special characters.
    : Return: The modified string with special characters removed.
    """
    cleaned_string = ""
    clean_chars = "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789 "
    for char in string:
        if char in clean_chars:
            cleaned_string += char
    return cleaned_string